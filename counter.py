import flet as ft

def main(page: ft.Page):
    page.title = "Flet First Project"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    txt_number = ft.TextField(value= "0", text_align= ft.TextAlign.RIGHT, width=100)

    def click_minus(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def click_add(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()


    page.add(
        ft.Row(
            [
                ft.IconButton(ft.Icons.REMOVE, on_click=click_minus),
                txt_number,
                ft.IconButton(ft.Icons.ADD, on_click=click_add),
            ],
            alignment= ft.MainAxisAlignment.CENTER,
        )
    )


ft.app(main)