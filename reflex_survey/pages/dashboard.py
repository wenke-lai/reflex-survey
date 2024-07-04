"""The dashboard page."""

import reflex as rx

from reflex_survey.templates import template


class DashboardState(rx.State):
    value: int = 0

    def increment(self):
        self.value += 1

    def decrement(self):
        self.value -= 1


@template(route="/dashboard", title="Dashboard")
def dashboard() -> rx.Component:
    """The dashboard page.

    Returns:
        The UI for the dashboard page.
    """
    return rx.vstack(
        rx.heading("Dashboard", size="8"),
        rx.text("Welcome to Reflex!"),
        rx.text(
            "You can edit this page in ",
            rx.code("{your_app}/pages/dashboard.py"),
        ),
        rx.button("++", on_click=DashboardState.increment),
        rx.text(DashboardState.value),
        rx.button("--", on_click=DashboardState.decrement),
    )
