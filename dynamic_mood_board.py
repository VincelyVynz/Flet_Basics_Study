import flet as ft
import random

def main(page: ft.Page):
    page.title = "Dynamic Mood Board"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER

    # Quotes

    calm_quotes = [
        "Stability starts with a clear mind.",
        "Slow is smooth; smooth is fast.",
        "Clarity emerges when noise drops.",
        "Own the moment, not the momentum.",
        "Calm is a competitive advantage."
    ]

    energetic_quotes = [
        "Execute with velocity.",
        "Momentum drives outcomes.",
        "Push past the comfort ceiling.",
        "Speed unlocks opportunity.",
        "Energy scales impact."
    ]

    focused_quotes = [
        "Eliminate noise. Prioritize what moves the needle.",
        "Attention is your highest-value asset.",
        "Precision beats volume.",
        "Stay locked in on the core deliverable.",
        "Focus converts effort into results."
    ]


    # UI

    headline = ft.Text("Select a mood to begin", size = 28, weight = ft.FontWeight.BOLD, color="black")
    emoji = ft.Text("🙂", size=50)
    quote_text = ft.Text("Your mood-driven quote will appear here", size= 20, italic=True, color="black")


    # mood change function

    def mood_change(e):
        mood = mood_dropdown.value

        if mood == "Calm":
            page.bgcolor = "#CFE8FC"
            headline.value = "Calm Mode"
            emoji_value = "😌"
            quote_text.value = random.choice(calm_quotes)

        elif mood == "Energetic":
            page.bgcolor = "#FFE9B3"
            headline.value = "Energetic Mode"
            emoji_value = "😃"
            quote_text.value = random.choice(energetic_quotes)

        elif mood == "Focused":
            page.bgcolor = "#D4F5D0"
            headline.value = "Focused Mode"
            emoji_value = "😎"
            quote_text.value = random.choice(focused_quotes)

        page.update()

    mood_dropdown = ft.Dropdown(
        label="Choose your mood",
        tooltip="Choose your mood",
        width=300,
        color = "black",
        options=[
            ft.dropdown.Option("Calm"),
            ft.dropdown.Option("Energetic"),
            ft.dropdown.Option("Focused"),
        ]
    )

    def shuffle_quote(e):
        mood = mood_dropdown.value
        if mood == "Calm":
            quote_text.value = random.choice(calm_quotes)
        elif mood == "Energetic":
            quote_text.value = random.choice(energetic_quotes)
        elif mood == "Focused":
            quote_text.value = random.choice(focused_quotes)
        page.update()


    mood_dropdown.on_change = mood_change

    shuffle_btn = ft.ElevatedButton("Get another quote", on_click=shuffle_quote)

    page.add(
        ft.Row(
            [
                headline,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),

        ft.Row(
            [
            emoji,
            mood_dropdown,
            ],
            alignment= ft.MainAxisAlignment.CENTER,
        ),

        ft.Row(
            [
                quote_text,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10,
        ),

        ft.Row(
            [
                shuffle_btn,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10,
        )

    )










ft.app(main)