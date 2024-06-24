import flet as ft

def main(page: ft.Page):
    page.bgcolor = ft.colors.WHITE
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.fonts = {
        "Roboto": "https://github.com/google/fonts/blob/main/apache/robotomono/RobotoMono%5Bwght%5D.ttf",
    }

    main_text = ft.SafeArea(ft.Text("Have a good training session!".upper(),
                                    color='#363636', size=20, weight=ft.FontWeight.BOLD, font_family="Roboto", text_align=ft.TextAlign.CENTER))
    start_button = ft.OutlinedButton(content=ft.Text("Start".upper(),
                                                    size=16, weight=ft.FontWeight.NORMAL, font_family="Roboto", text_align=ft.TextAlign.CENTER),
                                     style=ft.ButtonStyle(
                                         color={
                                             ft.ControlState.DEFAULT: "#515151",
                                         },
                                         overlay_color="#cdcdcd",
                                         shadow_color="#000000",
                                         elevation=3,
                                         shape=ft.RoundedRectangleBorder(5),
                                         bgcolor="#ffffff",
                                         padding=0
                                     ),
                                     width=200, height=30)
    
    settings_button = ft.OutlinedButton(content=ft.Text("Settings".upper(),
                                                    size=16, weight=ft.FontWeight.NORMAL, font_family="Roboto", text_align=ft.TextAlign.CENTER),
                                     style=ft.ButtonStyle(
                                         color={
                                             ft.ControlState.DEFAULT: "#515151",
                                         },
                                         overlay_color="#cdcdcd",
                                         shadow_color="#000000",
                                         elevation=3,
                                         shape=ft.RoundedRectangleBorder(5),
                                         bgcolor="#ffffff",
                                         padding=0
                                     ),
                                     width=200, height=30)

    buttons = ft.Column(controls=[start_button, settings_button], spacing=10)
    page.add(main_text, buttons)

if __name__ == "__main__":
    ft.app(target=main)