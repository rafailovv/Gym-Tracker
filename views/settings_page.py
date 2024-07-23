import flet as ft


class SettingsPage:
    """ Class For Settings Page """

    def __init__(self, page: ft.Page,
                 settings,
                 routes={"start_page_route": "/"}) -> None:
        def change_language(e):
            """ Define language picker behavior """

            current_language = language_picker.controls[language_picker.selected_index].value
            language_button.content.value = current_language

            if current_language == "English":
                self.settings.lang_preset = self.settings.set_language("en")
                self.settings.lang = "en"
            elif current_language == "Russian":
                self.settings.lang = "ru"
                self.settings.lang_preset = self.settings.set_language("ru")

            language_button.update()

        self.page = page
        self.routes = routes
        self.settings = settings

        lang_preset = self.settings.lang_preset
        
        title = ft.Text(
                    lang_preset["SETTINGS_HEADER"].upper(),
                    color='#363636', size=25, weight=ft.FontWeight.BOLD, font_family="Roboto Mono", text_align=ft.TextAlign.CENTER)
        
        back_button = ft.IconButton(
            icon=ft.icons.ARROW_BACK_OUTLINED, icon_color="#515151", icon_size=25,
            style=ft.ButtonStyle(overlay_color="#cdcdcd"),
            on_click=lambda _: self.page.go(self.routes["start_page_route"]))
        
        top = ft.SafeArea(
            ft.Row(
                [title, back_button],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.CrossAxisAlignment.START))
        
        language_variants = ["English", "Russian"]

        lang_index = 0
        if self.settings.lang == "ru":
            lang_index = 1
            
        language_picker = ft.CupertinoPicker(
            controls=[ft.Text(lang) for lang in language_variants],
            selected_index=lang_index,
            magnification=1.22,
            squeeze=1.2,
            use_magnifier=True,
            on_change=change_language)
        
        language_title = ft.Text(
            lang_preset["SETTINGS_LANG_TITLE"].capitalize(),
            color="#363636", size=20, weight=ft.FontWeight.NORMAL, font_family="Roboto Mono", text_align=ft.TextAlign.CENTER)

        language_button = ft.TextButton(
            content=ft.Text(
                language_picker.controls[language_picker.selected_index].value.capitalize(),
                color="#363636", size=20, weight=ft.FontWeight.NORMAL, font_family="Roboto Mono", text_align=ft.TextAlign.CENTER),
            style=ft.ButtonStyle(overlay_color="#cdcdcd"),
            on_click=lambda e: self.page.open(
                ft.CupertinoBottomSheet(
                    language_picker,
                    height=200)))
        
        language_setting = ft.Row(
            [language_title, language_button],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER)

        settings_content = ft.Column(
            [language_setting],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        
        self.setting_page_view = ft.View(
            "/settings",
            [top, settings_content],
            bgcolor="#ffffff")
    

    def get_view(self):
        """ Returns view """
        
        return self.setting_page_view