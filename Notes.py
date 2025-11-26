import flet as ft

def main(page: ft.Page):
    page.title = "Notes"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    greeting = "Welcome User!"
    session_id = page.session_id

    notes_column = ft.Column()


    note = ft.TextField()

    def add_note(e):
        notes_column.controls.append(note)
        page.update()

    add_button = ft.ElevatedButton(on_click= add_note, text="Add Note")

    page.add(
        ft.Row(
            [
                ft.Text(greeting),
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [
                ft.Text(f"Session ID: {session_id}"),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Row(
            [
                add_button,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )


ft.app(main)