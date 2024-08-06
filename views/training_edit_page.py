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

            for exercise in self.session_exercises:
                exercise_info = []
                title, *exercise_info = exercise
                session[self.session_title]["order"].append(title)

                if exercise_info[0] == "setsXreps":
                    session[self.session_title]["sets"][title] = {
                        "set_count": int(exercise_info[1]),
                        "repeat_count_per_set": int(exercise_info[2])
                    }
                elif exercise_info[0] == "time":
                    session[self.session_title]["time"][title] = int(exercise_info[1])
            
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
        for exercise in self.session_exercises:
            session_exercises_items.append(self._create_exercise_item(exercise))
        
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
    

    def _get_session_exercises(self, session_data: dict) -> list:
        """ Return list with current session exercises """

        session = []
        
        for title in session_data["order"]:
            if "sets" in session_data and title in session_data["sets"]:
                set_count = session_data["sets"][title]["set_count"]
                reps_count = session_data["sets"][title]["repeat_count_per_set"]
                session.append((title, "setsXreps", set_count, reps_count))
            elif "time" in session_data and title in session_data["time"]:
                seconds = session_data["time"][title]
                session.append((title, "time", seconds))

        return session
    

    def _create_exercise_item(self, exercise_data: tuple):
        """ Creates Exercise Control """
        def delete_exercise(exercise_title: str, exercise: ft.Container):
            """ Trigger For Delete Button """
            index = None
            for i in range(len(self.session_exercises)):
                if self.session_exercises[i][0] == exercise_title:
                    index = i
                    break
            
            if index is not None:
                self.session_exercises.pop(i)
            
            exercise.disabled = True
            exercise.visible = False
            exercise.update()


        title, exercise_type = exercise_data[0], exercise_data[1]

        delete_button = ft.IconButton(
            icon=ft.icons.DELETE, icon_color="#515151", icon_size=25,
            style=ft.ButtonStyle(
                overlay_color="#cdcdcd"))

        if exercise_type == "setsXreps":
            sets_count, reps_count = exercise_data[2], exercise_data[3]

            exercise_title = ft.Text(
                title.capitalize(),
                color="#363636", size=20, weight=ft.FontWeight.NORMAL, font_family="Roboto Mono", text_align=ft.TextAlign.CENTER)
            
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
                cursor_color="#cdcdcd")

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
                cursor_color="#cdcdcd")

            exercise_controls = ft.Row(
                [delete_button,
                 exercise_sets,
                 ft.Text("X",
                         color='#363636', size=20, weight=ft.FontWeight.BOLD, font_family="Roboto Mono", text_align=ft.TextAlign.CENTER),
                exercise_reps],
                alignment=ft.MainAxisAlignment.END,
                vertical_alignment=ft.CrossAxisAlignment.CENTER)
        elif exercise_type == "time":
            seconds = exercise_data[2]

            exercise_title = ft.Text(
                title.capitalize(),
                color="#363636", size=20, weight=ft.FontWeight.NORMAL, font_family="Roboto Mono", text_align=ft.TextAlign.CENTER)
            
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
                placeholder_text="Set count",
                placeholder_style=ft.TextStyle(size=25, color="#cdcdcd", font_family="Roboto Mono"),
                cursor_color="#cdcdcd")
            
            exercise_controls = ft.Row(
                [delete_button, exercise_time],
                alignment=ft.MainAxisAlignment.END,
                vertical_alignment=ft.CrossAxisAlignment.CENTER)
        
        delete_button.on_click = lambda _: delete_exercise(title, exercise)
            
        exercise = ft.Container(
            ft.Row(
                [exercise_title, exercise_controls],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.CrossAxisAlignment.CENTER),
            padding=10,
            border=ft.Border(top=ft.BorderSide(1, "#cdcdcd"), bottom=ft.BorderSide(1, "#cdcdcd")))
        
        return exercise
    
    def get_view(self):
        """ Returns view """

        return self.training_edit_view