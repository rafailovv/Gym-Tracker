import flet as ft


class TrainingPage:
    """ Class For Training Page View Usage """

    def __init__(self, page: ft.Page, routes={"trainings_add_page_route": "/trainings/add",
                                              "trainings_session_page_route": "/trainings/"}):
        self.page = page
        self.routes = routes
        
        back_button_container = ft.Container(ft.IconButton(icon=ft.icons.ARROW_BACK_IOS_NEW, icon_color="#363636", icon_size=25, tooltip="Back",
                                    style=ft.ButtonStyle(
                                        overlay_color="#cdcdcd"
                                    ),
                                    on_click=lambda _: self.page.go(self.page.views[-2].route)),
                                    alignment=ft.alignment.top_left)
        back_button = ft.SafeArea(back_button_container)

        main_text_container = ft.Container(ft.Text("Choose your training for today!".upper(),
                                    color='#363636',
                                    size=20, weight=ft.FontWeight.BOLD, font_family="Roboto Mono", text_align=ft.TextAlign.CENTER),
                                    alignment=ft.alignment.center)
        main_text = ft.SafeArea(main_text_container)


        training_cards_grid = ft.GridView(
            max_extent=150,
            spacing=10,
            run_spacing=10
        )
        
        # See trainings structure in board or notebook
        trainings = {}
        if page.client_storage.contains_key("trainings"):
            trainings = self.page.client_storage.get("trainings")
        
        training_cards = []
        for training_title in trainings:
            training_cards.append(self._create_training_card(training_title, trainings[training_title]["src"]))

        plus_card = self._create_training_card("Add Training", "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Plus_symbol.svg/1200px-Plus_symbol.svg.png", plus=True)
        training_cards.append(plus_card)
        training_cards_grid.controls = training_cards
         
        self.training_page_view = ft.View("/trainings", [back_button, main_text, training_cards_grid],
                                          bgcolor="#ffffff")
    

    def _create_training_card(self, title, src, plus=False):
        training_card_image = ft.Image(src=src,
                                       width=150, height=70,
                                       fit=ft.ImageFit.CONTAIN)
        training_card_text = ft.Text(value=title,
                                     width=150,
                                     color="#515151",
                                     size=16, weight=ft.FontWeight.NORMAL, font_family="Roboto Mono", text_align=ft.TextAlign.CENTER)

        training_card_content = ft.Column([training_card_image, training_card_text], spacing=10)

        training_card = ft.Container(width=150, height=150, bgcolor="#ffffff",
                                     border=ft.Border(ft.BorderSide(width=0.75, color="#cdcdcd"), ft.BorderSide(width=0.75, color="#cdcdcd"), ft.BorderSide(width=0.75, color="#cdcdcd"), ft.BorderSide(width=0.75, color="#cdcdcd")),
                                     border_radius=ft.BorderRadius(5, 5, 5, 5),
                                     shadow=ft.BoxShadow(spread_radius=0, blur_radius=0.1, color="#000000", blur_style=ft.ShadowBlurStyle.NORMAL),
                                     alignment=ft.alignment.center,
                                     content=training_card_content,
                                     padding=5,
                                     adaptive=True,
                                     on_click=lambda _: self.page.go(f"{self.routes["trainings_session_page_route"]}{title}" if not(plus) else self.routes["trainings_add_page_route"]))
        return training_card
    
    
    def get_view(self):
        return self.training_page_view