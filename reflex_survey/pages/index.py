"""The home page of the app."""

import reflex as rx

from reflex_survey import styles
from reflex_survey.templates import template

from .dashboard import DashboardState


@template(route="/", title="Home")
def index() -> rx.Component:
    """The home page.

    Returns:
        The UI for the home page.
    """
    with open("README.md", encoding="utf-8") as readme:
        content = readme.read()
    return rx.vstack(
        rx.text(DashboardState.value),
        rx.markdown(content, component_map=styles.markdown_style),
    )
