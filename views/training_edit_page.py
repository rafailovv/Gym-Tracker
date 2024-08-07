import flet as ft


class TrainingEditPage():
    """ Class For Editing Existing Training Session """

    def __init__(self, page: ft.Page,
                 session_title: str,
                 session_data: dict,
                 routes={"trainings_page_route": "/trainings"}) -> None:
        def complete_changes(e) -> None:
            session = self.page.client_storage.get("trainings")
            
            if not self.session_exercises: # Empty session
                del session[self.session_title]
                self.page.client_storage.set("trainings", session)
                self.page.go(self.routes["trainings_page_route"])
                return
            
            session[self.session_title]["order"] = []
            session[self.session_title]["sets"] = {}
            session[self.session_title]["time"] = {}

            for title in self.session_exercises:
                session[self.session_title]["order"].append(title)

                if "sets" in self.session_exercises[title] and "reps" in self.session_exercises[title]:
                    session[self.session_title]["sets"][title] = {
                        "set_count": int(self.session_exercises[title]["sets"]),
                        "repeat_count_per_set": int(self.session_exercises[title]["reps"])
                    }
                elif "time" in self.session_exercises[title]:
                    session[self.session_title]["time"][title] = int(self.session_exercises[title]["time"])
            
            self.page.client_storage.set("trainings", session)
            self.page.go(self.routes["training_page"])


        self.page = page
        self.session_title = session_title
        self.session_data = session_data

        routes["training_page"] = f"/trainings/{self.session_title}"
        self.routes = routes

        trainings_title = ft.Text(
            f"{self.session_title}".upper(),
            color='#363636', size=25, weight=ft.FontWeight.BOLD, font_family="Roboto Mono", text_align=ft.TextAlign.CENTER)
        
        trainings_complete_button = ft.IconButton(
            icon=ft.icons.CHECK_OUTLINED, icon_color="#515151", icon_size=25,
            style=ft.ButtonStyle(
                overlay_color="#cdcdcd"),
            on_click=complete_changes)

        trainings_top = ft.SafeArea(
            ft.Row(
                [trainings_title, trainings_complete_button],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN, vertical_alignment=ft.CrossAxisAlignment.CENTER))
        
        self.session_exercises = self._get_session_exercises(self.session_data)
        session_exercises_items = []
        for title in self.session_exercises:
            session_exercises_items.append(self._create_exercise_item(title, self.session_exercises[title]))
        
        session_list = ft.Container(
            ft.Column(
                session_exercises_items,
                spacing=10,
                alignment=ft.MainAxisAlignment.START, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            padding=10)

        self.training_edit_view = ft.View(
            f"/trainings/{self.session_title}/edit",
            [trainings_top, session_list],
            bgcolor="#ffffff",
            scroll=ft.ScrollMode.ADAPTIVE)
    

    def _get_session_exercises(self, session_data: dict) -> dict:
        """ Return list with current session exercises """

        session = {}
        for title in session_data["order"]:
            if "sets" in session_data and title in session_data["sets"]:
                set_count = session_data["sets"][title]["set_count"]
                reps_count = session_data["sets"][title]["repeat_count_per_set"]
                session[title] = {"sets": set_count,
                                  "reps": reps_count}
            elif "time" in session_data and title in session_data["time"]:
                seconds = session_data["time"][title]
                session[title] = {"time": seconds}

        return session
    

    def _create_exercise_item(self, exercise_title: str, exercise_data) -> ft.Container:
        """ Creates Exercise Control """
        def delete_exercise(exercise_title: str, exercise: ft.Container) -> None:
            """ Trigger For Delete Button """

            if exercise_title in self.session_exercises:
                del self.session_exercises[exercise_title]

            exercise.disabled = True
            exercise.visible = False
            exercise.update()
        

        def change_field(e, exercise_title: str, field_type: str) -> None:
            if "sets" == field_type:
                self.session_exercises[exercise_title]["sets"] = int(e.data) if e.data != "" else 0
            elif "reps" == field_type:
                self.session_exercises[exercise_title]["reps"] = int(e.data) if e.data != "" else 0
            elif "time" == field_type:
                self.session_exercises[exercise_title]["time"] = int(e.data) if e.data != "" else 0


        delete_button = ft.IconButton(
            icon=ft.icons.DELETE, icon_color="#515151", icon_size=25,
            style=ft.ButtonStyle(
                overlay_color="#cdcdcd"))
        
        exercise_title_item = ft.Text(
            exercise_title.capitalize(),
            color="#363636", size=20, weight=ft.FontWeight.NORMAL, font_family="Roboto Mono", text_align=ft.TextAlign.CENTER)
        
        if "sets" in exercise_data and "reps" in exercise_data:
            sets_count, reps_count = exercise_data["sets"], exercise_data["reps"]

            exercise_sets = ft.CupertinoTextField(
                width=35,
                value=sets_count,
                text_style=ft.TextStyle(size=16, color="#e6e6e6", font_family="Roboto Mono", letter_spacing=1.5),
                input_filter=ft.NumbersOnlyInputFilter(),
                capitalization=ft.TextCapitalization.CHARACTERS,
                max_length=30,
                max_lines=1,
                text_align=ft.TextAlign.CENTER,
                bgcolor="#4f4e4e",
                border=ft.Border(ft.BorderSide(0.75, "#515151"), ft.BorderSide(0.75, "#515151"), ft.BorderSide(0.75, "#515151"), ft.BorderSide(0.75, "#515151")),
                focused_border_color="#363636",
                focused_border_width=0.75,
                placeholder_text="Set count",
                placeholder_style=ft.TextStyle(size=25, color="#cdcdcd", font_family="Roboto Mono"),
                cursor_color="#cdcdcd",
                on_change=lambda e: change_field(e, exercise_title, "sets"))
            
            exercise_reps = ft.CupertinoTextField(
                width=35,
                value=reps_count,
                text_style=ft.TextStyle(size=16, color="#e6e6e6", font_family="Roboto Mono", letter_spacing=1.5),
                input_filter=ft.NumbersOnlyInputFilter(),
                capitalization=ft.TextCapitalization.CHARACTERS,
                max_length=30,
                max_lines=1,
                text_align=ft.TextAlign.CENTER,
                bgcolor="#4f4e4e",
                border=ft.Border(ft.BorderSide(0.75, "#515151"), ft.BorderSide(0.75, "#515151"), ft.BorderSide(0.75, "#515151"), ft.BorderSide(0.75, "#515151")),
                focused_border_color="#363636",
                focused_border_width=0.75,
                placeholder_text="Rep count",
                placeholder_style=ft.TextStyle(size=25, color="#cdcdcd", font_family="Roboto Mono"),
                cursor_color="#cdcdcd",
                on_change=lambda e: change_field(e, exercise_title, "reps"))

            exercise_controls = ft.Row(
                [delete_button,
                exercise_sets,
                ft.Text("X",
                        color='#363636', size=20, weight=ft.FontWeight.BOLD, font_family="Roboto Mono", text_align=ft.TextAlign.CENTER),
                exercise_reps],
                alignment=ft.MainAxisAlignment.END,
                vertical_alignment=ft.CrossAxisAlignment.CENTER)
        elif "time" in exercise_data:
            seconds = exercise_data["time"]

            exercise_time = ft.CupertinoTextField(
                width=75,
                value=seconds,
                text_style=ft.TextStyle(size=16, color="#e6e6e6", font_family="Roboto Mono", letter_spacing=1.5),
                input_filter=ft.NumbersOnlyInputFilter(),
                capitalization=ft.TextCapitalization.CHARACTERS,
                max_length=30,
                max_lines=1,
                text_align=ft.TextAlign.CENTER,
                bgcolor="#4f4e4e",
                border=ft.Border(ft.BorderSide(0.75, "#515151"), ft.BorderSide(0.75, "#515151"), ft.BorderSide(0.75, "#515151"), ft.BorderSide(0.75, "#515151")),
                focused_border_color="#363636",
                focused_border_width=0.75,
                placeholder_text="Time (in seconds)",
                placeholder_style=ft.TextStyle(size=25, color="#cdcdcd", font_family="Roboto Mono"),
                cursor_color="#cdcdcd",
                on_change=lambda e: change_field(e, exercise_title, "time"))
            
            exercise_controls = ft.Row(
                [delete_button, exercise_time],
                alignment=ft.MainAxisAlignment.END,
                vertical_alignment=ft.CrossAxisAlignment.CENTER)
            
        exercise = ft.Container(
            ft.Row(
                [exercise_title_item, exercise_controls],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.CrossAxisAlignment.CENTER),
            padding=10,
            border=ft.Border(top=ft.BorderSide(1, "#cdcdcd"), bottom=ft.BorderSide(1, "#cdcdcd")))
        
        delete_button.on_click = lambda _: delete_exercise(exercise_title, exercise)

        return exercise
    

    def get_view(self):
        """ Returns view """

        return self.training_edit_view