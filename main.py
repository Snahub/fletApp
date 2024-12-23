import flet as ft

def main(page: ft.Page):
    page.title = "Test Flet App"
    page.add(ft.Text("Hello, Flet!"))

ft.app(target=main ) 