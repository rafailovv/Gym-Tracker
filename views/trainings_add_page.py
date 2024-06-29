import flet as ft


class TrainingsAddPage:
    """ Class For Addition Of Training """

    def __init__(self, page: ft.Page, routes={"trainings_page_route": "/trainings"}):
        self.page = page
        self.routes = routes

        trainings_add_confirm_button = ft.IconButton(icon=ft.icons.CHECK, icon_color="#1eff00", icon_size=25,
                                                     style=ft.ButtonStyle(
                                                         overlay_color="#cdcdcd"
                                                     ),
                                                     on_click=lambda _: self.page.go(self.routes["trainings_page_route"]))
        trainings_add_title = ft.TextField(
            label="Training Title", text_size=20, max_length=30, max_lines=1, text_align=ft.TextAlign.LEFT,
            text_style=ft.TextStyle(color="#363636", font_family="Roboto Mono"),
            label_style=ft.TextStyle(color="#363636", font_family="Roboto Mono"),
            counter_style=ft.TextStyle(color="#363636", font_family="Roboto Mono"),
            focused_border_color="#363636",
            focused_border_width=1)
        
        trainings_add_top = ft.SafeArea(ft.Column(controls=[trainings_add_confirm_button, trainings_add_title],
                                                  alignment=ft.MainAxisAlignment.START,
                                                  horizontal_alignment=ft.CrossAxisAlignment.END))
        
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