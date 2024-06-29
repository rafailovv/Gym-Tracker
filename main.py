import flet as ft

from views.start_page import StartPage
from views.trainings_page import TrainingPage
from views.trainings_add_page import TrainingsAddPage

def main(page: ft.Page):
    """ App Entry Point Function """

    page.bgcolor = ft.colors.WHITE
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    page.fonts = {
        "Roboto Mono": "https://github.com/google/fonts/raw/main/apache/robotomono/RobotoMono%5Bwght%5D.ttf",
        "Roboto Slab": "https://github.com/google/fonts/raw/main/apache/robotoslab/RobotoSlab%5Bwght%5D.ttf",
        "Kanit": "https://raw.githubusercontent.com/google/fonts/master/ofl/kanit/Kanit-Bold.ttf",
    }
    
    # See trainings structure in board or notebook
    page.client_storage.set("trainings", {"Cardio": {"src": "https://cdn.icon-icons.com/icons2/2487/PNG/512/cardio_workout_icon_150073.png"}})
    page.update()

    start_page = StartPage(page)
    start_page_view = start_page.get_view()

    training_page = TrainingPage(page)
    training_page_view = training_page.get_view()

    training_add_page = TrainingsAddPage(page)
    training_add_page_view = training_add_page.get_view()

    def route_change(route):
        page.views.clear()
        page.views.append(start_page_view)

        if page.route == "/trainings":
            page.views.append(training_page_view)
        elif page.route == "/trainings/add":
            page.views.append(training_add_page_view)

        page.update()
    
    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


if __name__ == "__main__":
    ft.app(target=main)