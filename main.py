import string
import secrets
import flet as ft

from flet import TextField


def main(page: ft.Page):
    page.title = "ГЕНЕРАТОР"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    # Выравниваем элементы по центру горизонтально, чтобы было красиво
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.theme = ft.Theme(
        color_scheme_seed=ft.Colors.RED,
    )
    page.window.width = 500
    page.window.height = 500

    field = TextField(
        label="Ваш пароль",
        read_only=True,
        text_align=ft.TextAlign.CENTER,
        text_style=ft.TextStyle(size=18, weight=ft.FontWeight.BOLD)
    )


    def generate(e, length=12):
        a = string.ascii_letters + string.digits + string.punctuation
        password = "".join(secrets.choice(a) for _ in range(length))
        field.value = password
        page.update()


    Button = ft.TextButton("сгенерировать", on_click=generate)


    page.add(field, Button)


if __name__ == "__main__":
    ft.run(main)
