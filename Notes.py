import flet as ft
from datetime import datetime
import time
import uuid


def main(page: ft.Page):
    page.title = "Notes Taker"
    page.vertical_alignment = ft.MainAxisAlignment.START

    session_id = str(uuid.uuid4())[:8]
    session_start = time.time()

    lbl_session = ft.Text(f"Session ID: {session_id}")
    lbl_elapsed = ft.Text(f"Session active for: 0s")

    note_input = ft.TextField(label= "Write your note", expand= True)
    add_button = ft.ElevatedButton(text= "Add Note")

    notes_column = ft.Column(spacing= 8)

    def add_note(e):
        text = note_input.value.strip()
        if not text:
            return

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        note_row = ft.Row(
            controls=[
                ft.Text(timestamp, width=170),
                ft.Text(text, expand= True),
                ft.IconButton(ft.Icons.DELETE, tooltip= "Delete")
            ],
            alignment=ft.MainAxisAlignment.START
        )

        def delete_note(ev):
            notes_column.controls.remove(note_row)
            page.update()

        note_row.controls[2].on_click = delete_note

        notes_column.controls.append(note_row)
        note_input.value = ""
        page.update()

    add_button.on_click = add_note


    page.add(
        ft.Row(
            [
                lbl_session, ft.Column([lbl_elapsed, notes_column])
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            ),
        ft.Row(
            [
                note_input, add_button
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        notes_column
    )

    def tick_timer(ev):
        elapsed = int(time.time() - session_start)
        lbl_elapsed.value = f"Session active for: {elapsed}s"
        page.update()

    timer = ft.Timer(interval = 1, repeat = True, on_tick= tick_timer)
    page.add(timer)


ft.app(main)