"""
All constants specific to the application
"""
from app.utils.env import env

APPLICATION = {
    "HOST_NAME": env("HOST_NAME", "0.0.0.0"),
    "HOST_PORT": env("HOST_PORT", "80")
}
