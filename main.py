import flet as ft
from views.start_page import StartPage


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
    page.update()

    start_page = StartPage(page, routes={"trainings_page_route": "/trainings",
                                     "settings_page_route": "/settings"})
    start_page_view = start_page.get_view()
    second_page_view = ft.View("/settings", [ft.Text("ASDASD", font_family="Roboto Mono"), ft.ElevatedButton("quit", on_click=lambda _: page.go("/"))])

    def route_change(route):
        page.views.clear()
        page.views.append(start_page_view)

        if page.route == "/settings":
            page.views.append(second_page_view)
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