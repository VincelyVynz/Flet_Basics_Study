import flet as ft
from flet.core.border_radius import horizontal


def main(page: ft.Page):
    page.title = "Notes App"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER

    # UI
    note_input = ft.TextField(
        label= "Write note",
        width= 300
    )

    notes_list = ft.Column()

    def add_note(e):
        value = note_input.value.strip()
        if not value:
            return

        notes_list.controls.append(ft.Text(value))

        note_input.value = ''
        note_input.focus()
        page.update()

    add_button = ft.ElevatedButton(
        text= "Add Note",
        on_click= add_note
    )

    page.add(
        ft.Container(
            width=400,
            padding=20,
            bgcolor=ft.Colors.with_opacity(0.05, ft.Colors.BLUE_GREY_900),
            border_radius=12,
            content=ft.Column(
                spacing=20,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    note_input,
                    add_button,
                    ft.Divider(),
                    ft.Text("Notes", size=22, weight=ft.FontWeight.BOLD),
                    ft.Container(
                        content=notes_list,
                        padding=10,
                        bgcolor=ft.Colors.with_opacity(0.04, ft.Colors.WHITE),
                        border_radius=8,
                        width=360,
                    ),
                ],
            ),
        )
    )


ft.app(main)
