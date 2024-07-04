"""Welcome to Reflex!."""

# Import all the pages.
import reflex as rx

from reflex_survey.pages import *  # noqa


class State(rx.State):
    """Define empty state to allow access to rx.State.router."""


# Create the app.
app = rx.App()
