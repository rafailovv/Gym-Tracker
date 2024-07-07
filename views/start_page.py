import flet as ft


class StartPage:
    """ Class For Start Page View Usage """

    def __init__(self, page: ft.Page, routes={"trainings_page_route": "/trainings",
                                     "settings_page_route": "/settings"}):
        self.page = page
        self.routes = routes

        main_text_container = ft.Container(ft.Text("Have a good training session!".upper(),
                                    color='#363636',
                                    size=20, weight=ft.FontWeight.BOLD, font_family="Roboto Mono", text_align=ft.TextAlign.CENTER),
                                    alignment=ft.alignment.center)
        main_text = ft.SafeArea(main_text_container)
        
        start_button = ft.OutlinedButton(content=ft.Text("Start".upper(),
                                                        size=16, weight=ft.FontWeight.NORMAL, font_family="Roboto Mono", text_align=ft.TextAlign.CENTER),
                                        width=200, height=30,
                                        style=ft.ButtonStyle(
                                            color="#515151",
                                            overlay_color="#cdcdcd",
                                            shadow_color="#000000",
                                            elevation=3,
                                            shape=ft.RoundedRectangleBorder(radius=5),
                                            bgcolor="#ffffff",
                                            padding=0
                                        ),
                                        on_click=lambda _: self.page.go(self.routes["trainings_page_route"]))
        
        settings_button = ft.OutlinedButton(content=ft.Text("Settings".upper(),
                                                        size=16, weight=ft.FontWeight.NORMAL, font_family="Roboto Mono", text_align=ft.TextAlign.CENTER),
                                        width=200, height=30,
                                        style=ft.ButtonStyle(
                                            color="#515151",
                                            overlay_color="#cdcdcd",
                                            shadow_color="#000000",
                                            elevation=3,
                                            shape=ft.RoundedRectangleBorder(radius=5),
                                            bgcolor="#ffffff",
                                            padding=0
                                        ),
                                        on_click=lambda _: self.page.go(self.routes["settings_page_route"]))
        buttons = ft.Column(controls=[start_button, settings_button], spacing=10)

        self.start_page_view = ft.View("/", [main_text, buttons],
                                bgcolor="#ffffff",
                                vertical_alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    

    def get_view(self):
        return self.start_page_view