import flet as ft


class TrainingsAddPage:
    """ Class For Addition Of Training """

    def __init__(self, page: ft.Page, routes={"trainings_page_route": "/trainings"}) -> None:
        def add_exercise(e) -> None:
            """ Addings exercise to training session logic """

            try:
                exercise_title = trainings_add_modal_exercise.controls[1].value
                exercise_type = trainings_add_modal_type.controls[1].text

                if exercise_title.strip() != "":
                    exercise_title = exercise_title.strip()

                    if exercise_type == variants[0]:
                        sets_count = int(trainings_add_modal_sets.controls[1].value)
                        reps_count = int(trainings_add_modal_reps.controls[1].value)

                        self.exercises.append({
                            "exercise_title": exercise_title,
                            "exercise_set_count": sets_count,
                            "exercise_repeat_count_per_set": reps_count})
                        
                        exercise_item_repeats = ft.Text(
                            f"{sets_count}X{reps_count}".upper(),
                            color="#363636", size=20, weight=ft.FontWeight.NORMAL, font_family="Roboto Mono", text_align=ft.TextAlign.CENTER)
                    elif exercise_type == variants[1]:
                        time = int(trainings_add_modal_time.controls[1].value) # TODO: Format (seconds) to (mm:ss)

                        self.exercises.append({
                            "exercise_title": exercise_title,
                            "exercise_time": time})
                        
                        exercise_item_repeats = ft.Text(
                            f"{time}".upper(),
                            color="#363636", size=20, weight=ft.FontWeight.NORMAL, font_family="Roboto Mono", text_align=ft.TextAlign.CENTER)
                    
                    exercise_item_title = ft.Text(
                        exercise_title.capitalize(),
                        color="#363636", size=20, weight=ft.FontWeight.NORMAL, font_family="Roboto Mono", text_align=ft.TextAlign.CENTER)
                    
                    exercise = ft.Container(
                        ft.Row(
                            [exercise_item_title, exercise_item_repeats],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER),
                        padding=10,
                        border=ft.Border(top=ft.BorderSide(1, "#cdcdcd"), bottom=ft.BorderSide(1, "#cdcdcd")))

                    trainings_exercises_list.controls.insert(-1, exercise)
                    trainings_exercises_list.update()

                    e.control.page.close(trainings_add_modal)
                else:
                    raise Exception("Title is empty")
            except:
                error = ft.CupertinoAlertDialog(
                    title=ft.Text(
                        "ERROR!",
                        color="#ff0000"),
                    actions=
                        [ft.CupertinoDialogAction(
                            "Ok",
                            on_click=lambda e: e.control.page.close(error))])
                
                e.control.page.open(error)
            finally:
                selected_type = variants[0]
                trainings_add_modal_type.controls[1].text = selected_type
                trainings_add_modal_exercise.controls[1].value = ""
                trainings_add_modal_sets.visible = True
                trainings_add_modal_sets.controls[1].value = ""
                trainings_add_modal_reps.visible = True
                trainings_add_modal_reps.controls[1].value = ""
                trainings_add_modal_time.visible = False
                trainings_add_modal_time.controls[1].value = ""


        def dismiss_dialog(e) -> None:
            """ Close dialog window """

            e.control.page.close(trainings_add_modal)
        

        def exercise_type_change(e) -> None:
            """ Select logic """

            trainings_add_modal_sets.controls[1].value = ""
            trainings_add_modal_reps.controls[1].value = ""
            trainings_add_modal_time.controls[1].value = ""

            if e.control.text == variants[0]:
                selected_type = variants[1]
                trainings_add_modal_sets.visible = False
                trainings_add_modal_reps.visible = False
                trainings_add_modal_time.visible = True
            else:
                selected_type = variants[0]
                trainings_add_modal_sets.visible = True
                trainings_add_modal_reps.visible = True
                trainings_add_modal_time.visible = False

            e.control.text = selected_type
            e.page.update()
        

        def finish_session(e) -> None:
            """ Ends training session creating and redirect to /trainings"""

            session_title = trainings_add_title.value
            session_title = session_title.capitalize()
            session_image_src = selected_photo.src

            if session_title.strip() != "" and self.exercises:
                session_title = session_title.strip()

                trainings = {}
                if self.page.client_storage.contains_key("trainings"):
                    trainings = self.page.client_storage.get("trainings")
                
                trainings[session_title] = {}
                trainings[session_title]["src"] = session_image_src

                for exercise in self.exercises:
                    if "exercise_time" in exercise:
                        if "time" not in trainings[session_title]:
                            trainings[session_title]["time"] = {}

                        trainings[session_title]["time"][exercise["exercise_title"]] = int(exercise["exercise_time"])
                    elif "exercise_set_count" in exercise and "exercise_repeat_count_per_set" in exercise:
                        if "sets" not in trainings[session_title]:
                            trainings[session_title]["sets"] = {}

                        trainings[session_title]["sets"][exercise["exercise_title"]] = {}
                        trainings[session_title]["sets"][exercise["exercise_title"]]["set_count"] = int(exercise["exercise_set_count"])
                        trainings[session_title]["sets"][exercise["exercise_title"]]["repeat_count_per_set"] = int(exercise["exercise_repeat_count_per_set"])
                    
                    if "order" not in trainings[session_title]:
                        trainings[session_title]["order"] = []

                    trainings[session_title]["order"].append(exercise["exercise_title"])
                
                self.page.client_storage.set("trainings", trainings)
                self.page.go(self.routes["trainings_page_route"])

        
        def image_pick_result(e):
            """ Set image picker photo """
            if e.files:
                selected_photo.src = e.files[0].path
            selected_photo.update()
        
        
        def image_pick_set_default(e):
            """ Sets image in photo picker to default """

            selected_photo.src = "https://upload.wikimedia.org/wikipedia/commons/1/18/Color-white.JPG"
            selected_photo.update()


        self.page = page
        self.routes = routes
        self.exercises = []

        trainings_add_confirm_button = ft.IconButton(
            icon=ft.icons.CHECK_OUTLINED, icon_color="#515151", icon_size=25,
            style=ft.ButtonStyle(overlay_color="#cdcdcd"),
            on_click=finish_session)
        
        trainings_back_button = ft.IconButton(
            icon=ft.icons.ARROW_BACK_OUTLINED, icon_color="#515151", icon_size=25,
            style=ft.ButtonStyle(overlay_color="#cdcdcd"),
            on_click=lambda _: self.page.go(self.routes["trainings_page_route"])
        )
        
        trainings_add_title = ft.CupertinoTextField(
            text_style=ft.TextStyle(size=25, color="#363636", font_family="Roboto Mono", letter_spacing=1.5),
            capitalization=ft.TextCapitalization.WORDS,
            max_length=30,
            max_lines=1,
            text_align=ft.TextAlign.LEFT,
            bgcolor="#ffffff",
            border=ft.Border(ft.BorderSide(0.75, "#515151"), ft.BorderSide(0.75, "#515151"), ft.BorderSide(0.75, "#515151"), ft.BorderSide(0.75, "#515151")),
            focused_border_color="#363636",
            focused_border_width=0.75,
            placeholder_text="Training Title".upper(),
            placeholder_style=ft.TextStyle(size=25, color="#cdcdcd", font_family="Roboto Mono"),
            cursor_color="#cdcdcd")
        
        trainings_add_top = ft.SafeArea(
            ft.Row(
                [trainings_add_title, trainings_back_button, trainings_add_confirm_button],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN, vertical_alignment=ft.CrossAxisAlignment.CENTER))

        variants = ["Set X Reps", "Time"]
        selected_type = variants[0]

        trainings_add_modal_exercise = ft.Row(
            [ft.Text(
                "Exercise title: ".capitalize(),
                color="#e6e6e6", size=14, weight=ft.FontWeight.NORMAL, font_family="Roboto Mono", text_align=ft.TextAlign.LEFT),
            ft.CupertinoTextField(
                width=100,
                text_style=ft.TextStyle(size=14, color="#e6e6e6", font_family="Roboto Mono", letter_spacing=1.5),
                capitalization=ft.TextCapitalization.WORDS,
                max_length=30,
                max_lines=1,
                text_align=ft.TextAlign.LEFT,
                bgcolor="#4f4e4e",
                border=ft.Border(ft.BorderSide(0.75, "#515151"), ft.BorderSide(0.75, "#515151"), ft.BorderSide(0.75, "#515151"), ft.BorderSide(0.75, "#515151")),
                focused_border_color="#363636",
                focused_border_width=0.75,
                cursor_color="#cdcdcd",)],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            visible=True)

        trainings_add_modal_type = ft.Row(
            [ft.Text(
                "Exercise type: ".capitalize(),
                color="#e6e6e6", size=14, weight=ft.FontWeight.NORMAL, font_family="Roboto Mono", text_align=ft.TextAlign.LEFT),
            ft.TextButton(
                text=selected_type,
                width=100,
                on_click=exercise_type_change)],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            visible=True)
        
        trainings_add_modal_sets = ft.Row(
            [ft.Text(
                "Sets: ".capitalize(),
                color="#e6e6e6", size=14, weight=ft.FontWeight.NORMAL, font_family="Roboto Mono", text_align=ft.TextAlign.LEFT),
            ft.CupertinoTextField(
                width=100,
                text_style=ft.TextStyle(size=14, color="#e6e6e6", font_family="Roboto Mono", letter_spacing=1.5),
                input_filter=ft.NumbersOnlyInputFilter(),
                capitalization=ft.TextCapitalization.CHARACTERS,
                max_length=30,
                max_lines=1,
                text_align=ft.TextAlign.LEFT,
                bgcolor="#4f4e4e",
                border=ft.Border(ft.BorderSide(0.75, "#515151"), ft.BorderSide(0.75, "#515151"), ft.BorderSide(0.75, "#515151"), ft.BorderSide(0.75, "#515151")),
                focused_border_color="#363636",
                focused_border_width=0.75,
                cursor_color="#cdcdcd",)],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            visible=True)

        trainings_add_modal_reps = ft.Row(
            [ft.Text(
                "Reps: ".capitalize(),
                color="#e6e6e6", size=14, weight=ft.FontWeight.NORMAL, font_family="Roboto Mono", text_align=ft.TextAlign.LEFT),
                ft.CupertinoTextField(
                    width=100,
                    text_style=ft.TextStyle(size=14, color="#e6e6e6", font_family="Roboto Mono", letter_spacing=1.5),
                    input_filter=ft.NumbersOnlyInputFilter(),
                    capitalization=ft.TextCapitalization.CHARACTERS,
                    max_length=30,
                    max_lines=1,
                    text_align=ft.TextAlign.LEFT,
                    bgcolor="#4f4e4e",
                    border=ft.Border(ft.BorderSide(0.75, "#515151"), ft.BorderSide(0.75, "#515151"), ft.BorderSide(0.75, "#515151"), ft.BorderSide(0.75, "#515151")),
                    focused_border_color="#363636",
                    focused_border_width=0.75,
                    cursor_color="#cdcdcd",)
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            visible=True
        )

        trainings_add_modal_time = ft.Row(
            [ft.Text(
                "Time (seconds): ".capitalize(),
                color="#e6e6e6", size=14, weight=ft.FontWeight.NORMAL, font_family="Roboto Mono", text_align=ft.TextAlign.LEFT),
            ft.CupertinoTextField(
                width=100,
                text_style=ft.TextStyle(size=14, color="#e6e6e6", font_family="Roboto Mono", letter_spacing=1.5),
                input_filter=ft.NumbersOnlyInputFilter(),
                capitalization=ft.TextCapitalization.CHARACTERS,
                max_length=30,
                max_lines=1,
                text_align=ft.TextAlign.LEFT,
                bgcolor="#4f4e4e",
                border=ft.Border(ft.BorderSide(0.75, "#515151"), ft.BorderSide(0.75, "#515151"), ft.BorderSide(0.75, "#515151"), ft.BorderSide(0.75, "#515151")),
                focused_border_color="#363636",
                focused_border_width=0.75,
                cursor_color="#cdcdcd",)],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            visible=False)

        trainings_add_modal_content = ft.Column(
            [trainings_add_modal_exercise, trainings_add_modal_type, trainings_add_modal_sets, trainings_add_modal_reps, trainings_add_modal_time])

        trainings_add_modal_actions = [
            ft.CupertinoDialogAction(
                "Yes",
                is_destructive_action=False,
                on_click=add_exercise,
            ),
            ft.CupertinoDialogAction(
                text="No",
                is_destructive_action=True,
                on_click=dismiss_dialog,
            )]

        trainings_add_modal = ft.CupertinoAlertDialog(
            title=ft.Text(
                "Exercise",
                color="#e6e6e6", size=20, weight=ft.FontWeight.NORMAL, font_family="Roboto Mono", text_align=ft.TextAlign.LEFT),
            content=trainings_add_modal_content,
            actions=trainings_add_modal_actions)
        
        trainings_session_image_picker = ft.FilePicker(
            on_result=image_pick_result)
        self.page.overlay.append(trainings_session_image_picker)
        
        trainings_session_image_picker_pick_button = ft.TextButton(
            content=ft.Text(
                "Pick image".capitalize(),
                color="#363636", size=20, weight=ft.FontWeight.NORMAL, font_family="Roboto Mono", text_align=ft.TextAlign.CENTER),
            style=ft.ButtonStyle(overlay_color="#cdcdcd"),
            on_click=lambda _: trainings_session_image_picker.pick_files(
                file_type=ft.FilePickerFileType.IMAGE))
        
        trainings_session_image_picker_default_button = ft.TextButton(
            content=ft.Text(
                "Set default".capitalize(),
                color="#363636", size=20, weight=ft.FontWeight.NORMAL, font_family="Roboto Mono", text_align=ft.TextAlign.CENTER),
            style=ft.ButtonStyle(overlay_color="#cdcdcd"),
            on_click=image_pick_set_default)
        
        trainings_session_image_picker_buttons = ft.Row(
            [trainings_session_image_picker_pick_button, trainings_session_image_picker_default_button],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.MainAxisAlignment.START)
        
        selected_photo = ft.Image(
            src="https://upload.wikimedia.org/wikipedia/commons/1/18/Color-white.JPG",
            width=300,
            height=140,
            fit=ft.ImageFit.CONTAIN)
        
        trainings_image_picker = ft.Column(
            [selected_photo, trainings_session_image_picker_buttons],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.STRETCH)

        trainings_add_exercise_button = ft.IconButton(
            icon=ft.icons.ADD_CIRCLE_OUTLINE, icon_color="#363636", icon_size=40,
            style=ft.ButtonStyle(overlay_color="#cdcdcd"),
            on_click=lambda e: e.control.page.open(trainings_add_modal))

        trainings_exercises_list = ft.Column(
            [trainings_add_exercise_button],
            alignment=ft.MainAxisAlignment.START, horizontal_alignment=ft.CrossAxisAlignment.STRETCH)
        
        self.trainings_add_view = ft.View(
            "/trainings/add",
            [trainings_add_top, trainings_image_picker, trainings_exercises_list],
            bgcolor="#ffffff",
            scroll=ft.ScrollMode.ADAPTIVE)
        

    def get_view(self):
        """ Returns view """

        return self.trainings_add_view