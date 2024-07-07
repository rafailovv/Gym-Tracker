import flet as ft


class TrainingsSessionPage:
    """ Class For Description Of Training Session """

    def __init__(self, page: ft.Page, session_title: str, session_data: dict, routes={"trainings_page_route": "/trainings"}) -> None:
        self.page = page
        self.session_title = session_title
        self.session_data = session_data
        self.routes = routes
        
        trainings_title = ft.SafeArea(ft.Text(f"{self.session_title}".upper(),
                                              color='#363636',
                                              size=30, weight=ft.FontWeight.BOLD, font_family="Roboto Mono", text_align=ft.TextAlign.CENTER))
        # Add session_data reading
        exercise_item_1 = self._create_exercise_item("Run", "1 min")
        exercise_item_2 = self._create_exercise_item("Kettle", "3x10")
        
        session_list = ft.Container(ft.Column(controls=[exercise_item_1, exercise_item_2],
                                              spacing=10,
                                              alignment=ft.MainAxisAlignment.START,
                                              horizontal_alignment=ft.CrossAxisAlignment.END),
                                    padding=10)

        self.trainings_session_view = ft.View(f"/trainings/{self.session_title}", [trainings_title, session_list],
                                          bgcolor="#ffffff")
    

    def _create_exercise_item(self, title, repeats):
        exercise_item_title = ft.Text(title.capitalize(),
                                                 color="#363636",
                                                 size=23, weight=ft.FontWeight.NORMAL, font_family="Roboto Mono", text_align=ft.TextAlign.CENTER)
        exercise_item_repeats = ft.Text(repeats.upper(),
                                                color="#363636",
                                                size=23, weight=ft.FontWeight.NORMAL, font_family="Roboto Mono", text_align=ft.TextAlign.CENTER)
        
        exercise_item = ft.Container(ft.Row(controls=[exercise_item_title, exercise_item_repeats],
                                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                            vertical_alignment=ft.CrossAxisAlignment.CENTER),
                                    padding=10,
                                    border=ft.Border(top=ft.BorderSide(1, "#cdcdcd"), bottom=ft.BorderSide(1, "#cdcdcd")))
        return exercise_item
    

    def get_view(self):
        return self.trainings_session_view