"""
All constants specific to the application
"""
from app.utils.env import env


APPLICATION = {
    "HOST_NAME": env("HOST_NAME", "0.0.0.0"),
    "HOST_PORT": env("HOST_PORT", "80"),
    "AUTHENTICATION_REQUIRED" : env("AUTHENTICATION_REQUIRED", "no"),
    "AUTHENTICATION_TOKEN" : env("AUTHENTICATION_TOKEN", ""),
    "AUTHENTICATION_API_KEY" : env("AUTHENTICATION_API_KEY", ""),    
}
