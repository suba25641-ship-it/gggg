import string
import secrets
import flet as ft
from flet import TextField


def main(page: ft.Page):
    page.title = "ГЕНЕРАТОР"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.theme = ft.Theme(
        color_scheme_seed=ft.Colors.RED_ACCENT,
    )
    page.window.width = 500
    page.window.height = 500

    # Переменная лимита внутри main
    click_left = 5

    field = TextField(
        label="Ваш пароль",
        read_only=True,
        text_align=ft.TextAlign.CENTER,
        text_style=ft.TextStyle(size=18, weight=ft.FontWeight.BOLD)
    )

    def generate(e, length=12):
        nonlocal click_left  # Позволяет изменять переменную из внешней функции main

        # Проверяем лимит ПЕРЕД генерацией
        if click_left <= 0:
            field.value = "Лимит исчерпан!"
            Button.disabled = True
            page.update()
            return

        # Уменьшаем счётчик
        click_left -= 1

        # Исправленные диапазоны для русских букв (1040-1071 для А-Я)
        russian_up = "".join(chr(i) for i in range(1040, 1072)) + "Ё"
        russian_low = "".join(chr(i) for i in range(1072, 1104)) + "ё"
        russian = russian_up + russian_low

        a = string.ascii_letters + string.digits + string.punctuation + russian
        password = "".join(secrets.choice(a) for _ in range(length))

        # Обновляем текст на кнопке и поле
        field.value = password
        Button.text = f"сгенерировать (Осталось: {click_left})"

        # Если это был последний клик — сразу гасим кнопку
        if click_left == 0:
            Button.disabled = True
            field.value = "Пароль создан. Лимит исчерпан!"

        page.update()

    # Сразу пишем на кнопке, сколько попыток есть изначально
    Button = ft.TextButton(f"сгенерировать (Осталось: {click_left})", on_click=generate)

    page.add(field, Button)


if __name__ == "__main__":
    ft.run(main)
