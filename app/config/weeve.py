"""
All constants specific to weeve
"""
from app.utils.env import env

WEEVE = {
    "MODULE_NAME": env("MODULE_NAME", "HTTP-Ingress"),
    "EGRESS_API_HOST": env("EGRESS_API_HOST", "http://localhost:8000")
}
