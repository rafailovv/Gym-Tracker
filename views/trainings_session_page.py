import flet as ft


class TrainingsSessionPage:
    """ Class For Description Of Training Session """

    def __init__(self, page: ft.Page, session_title: str, session_data: dict, routes={"trainings_page_route": "/trainings"}) -> None:
        self.page = page
        self.session_title = session_title
        self.session_data = session_data
        self.routes = routes
        
        # Add training session display
        self.trainings_session_view = ft.View(f"/trainings/{self.session_title}", [ft.SafeArea(ft.Text(f"{self.session_title}"))],
                                          bgcolor="#ffffff")

    def get_view(self):
        return self.trainings_session_view