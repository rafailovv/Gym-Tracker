import flet as ft


class TrainingsAddPage:
    """ Class For Addition Of Training """

    def __init__(self, page: ft.Page, routes={"trainings_page_route": "/trainings"}):
        self.page = page
        self.routes = routes

        trainings_add_confirm_button = ft.IconButton(icon=ft.icons.CHECK_CIRCLE_OUTLINE, icon_color="#515151", icon_size=25,
                                                     style=ft.ButtonStyle(
                                                         overlay_color="#cdcdcd"
                                                     ),
                                                     on_click=lambda _: self.page.go(self.routes["trainings_page_route"]))
        
        trainings_add_title = ft.CupertinoTextField(
            text_style=ft.TextStyle(size=25, color="#363636", font_family="Roboto Mono", letter_spacing=1.5),
            capitalization=ft.TextCapitalization.CHARACTERS,
            max_length=30, max_lines=1, text_align=ft.TextAlign.LEFT,
            bgcolor="#ffffff",
            border=ft.Border(ft.BorderSide(0.75, "#515151"), ft.BorderSide(0.75, "#515151"), ft.BorderSide(0.75, "#515151"), ft.BorderSide(0.75, "#515151")),
            focused_border_color="#363636",
            focused_border_width=0.75,
            placeholder_text="Training Title".upper(),
            placeholder_style=ft.TextStyle(size=25, color="#cdcdcd", font_family="Roboto Mono"),
            cursor_color="#cdcdcd")
        
        trainings_add_top = ft.SafeArea(ft.Row(controls=[trainings_add_title, trainings_add_confirm_button],
                                                  alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                                  vertical_alignment=ft.CrossAxisAlignment.CENTER))
        
        trainings_add_exercise_button = ft.IconButton(icon=ft.icons.ADD_CIRCLE_OUTLINE, icon_color="#363636", icon_size=40,
                                                      style=ft.ButtonStyle(
                                                         overlay_color="#cdcdcd"
                                                     ))
        trainings_exercises_list = ft.Column(controls=[trainings_add_exercise_button],
                                             alignment=ft.MainAxisAlignment.START,
                                             horizontal_alignment=ft.CrossAxisAlignment.STRETCH)
        
        self.trainings_add_view = ft.View("/trainings/add", [trainings_add_top, trainings_exercises_list],
                                          bgcolor="#ffffff")
        

    def get_view(self):
        return self.trainings_add_view