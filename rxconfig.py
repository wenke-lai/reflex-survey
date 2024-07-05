import reflex as rx
from reflex.constants import LogLevel

# Define the configuration for the Reflex app
# https://reflex.dev/docs/api-reference/config/

config = rx.Config(
    app_name="reflex_survey",
    loglevel=LogLevel.DEBUG,
    api_url="http://localhost:8000",  # The backend url the frontend will connect to.
    db_url="sqlite:///reflex.db",
    # redis_url="redis://localhost:6379/0",
    cors_allowed_origins=["*"],
    # disable telemetry
    telemetry_enabled=False,
)
