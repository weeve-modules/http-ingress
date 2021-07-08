"""
All constants specific to the application
"""
from app.utils.env import env


APPLICATION = {
    "HANDLER_HOST": env("HANDLER_HOST", "0.0.0.0"),
    "HANDLER_PORT": env("HANDLER_PORT", "80"),
}
