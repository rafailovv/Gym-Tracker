import flet as ft


class TrainingsSessionPage:
    """ Class For Description Of Training Session """

    def __init__(self, page: ft.Page,
                 session_title: str,
                 session_data: dict,
                 routes={"trainings_page_route": "/trainings"}) -> None:
        self.page = page
        self.session_title = session_title
        self.session_data = session_data

        routes["training_edit_route"] = f"/trainings/{self.session_title}/edit"
        self.routes = routes
        
        trainings_title = ft.Text(
            f"{self.session_title}".upper(),
            color='#363636', size=25, weight=ft.FontWeight.BOLD, font_family="Roboto Mono", text_align=ft.TextAlign.CENTER)
        
        trainings_back_button = ft.IconButton(
            icon=ft.icons.CANCEL_OUTLINED, icon_color="#515151", icon_size=25,
            style=ft.ButtonStyle(
                overlay_color="#cdcdcd"),
            on_click=lambda _: self.page.go(self.routes["trainings_page_route"]))
        
        trainings_edit_button = ft.IconButton(
            icon=ft.icons.EDIT_ROUNDED, icon_color="#515151", icon_size=25,
            style=ft.ButtonStyle(
                overlay_color="#cdcdcd"),
            on_click=lambda _: self.page.go(self.routes["training_edit_route"]))
        
        trainings_buttons = ft.Row(
            [trainings_edit_button, trainings_back_button],
            alignment=ft.MainAxisAlignment.END, vertical_alignment=ft.CrossAxisAlignment.CENTER)
        
        trainings_top = ft.SafeArea(
            ft.Row(
                [trainings_title, trainings_buttons],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN, vertical_alignment=ft.CrossAxisAlignment.CENTER))

        session_exercises = self._get_session_exercises(self.session_data)
        session_exercises_items = []
        for title, repeats in session_exercises:
            session_exercises_items.append(self._create_exercise_item(title, repeats))
        
        session_list = ft.Container(
            ft.Column(
                session_exercises_items,
                spacing=10,
                alignment=ft.MainAxisAlignment.START, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            padding=10)

        self.trainings_session_view = ft.View(
            f"/trainings/{self.session_title}",
            [trainings_top, session_list],
            bgcolor="#ffffff",
            scroll=ft.ScrollMode.ADAPTIVE)
    

    def _create_exercise_item(self, title: str, repeats: str) -> ft.Container:
        """ Returns exercise item section """

        exercise_item_title = ft.Text(
            title.capitalize(),
            color="#363636", size=20, weight=ft.FontWeight.NORMAL, font_family="Roboto Mono", text_align=ft.TextAlign.CENTER)
        
        exercise_item_repeats = ft.Text(
            repeats.upper(),
            color="#363636", size=20, weight=ft.FontWeight.NORMAL, font_family="Roboto Mono", text_align=ft.TextAlign.CENTER)
        
        exercise_item = ft.Container(
            ft.Row(
                [exercise_item_title, exercise_item_repeats],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN, vertical_alignment=ft.CrossAxisAlignment.CENTER),
            padding=10,
            border=ft.Border(top=ft.BorderSide(1, "#cdcdcd"), bottom=ft.BorderSide(1, "#cdcdcd")))
        
        return exercise_item
    

    def _get_session_exercises(self, session_data: dict) -> list:
        """ Return list with current session exercises """

        session = []
        
        for title in session_data["order"]:
            repeats = ""
            if "sets" in session_data and title in session_data["sets"]:
                repeats = f"{session_data["sets"][title]["set_count"]}X{session_data["sets"][title]["repeat_count_per_set"]}"
            elif "time" in session_data and title in session_data["time"]:
                seconds = session_data["time"][title]

                # Seconds to mm:ss
                minutes = seconds // 60
                seconds = seconds % 60
                
                repeats = ""
                if minutes < 10:
                    repeats = "0"
                repeats = repeats + f"{minutes}:"
                if seconds < 10:
                    repeats = repeats + "0"
                repeats = repeats + f"{seconds}"
            session.append((title, repeats))

        return session


    def get_view(self):
        """ Returns view """

        return self.trainings_session_view