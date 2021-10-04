"""
All route entry points
"""
from flask import Flask, request
import requests

from app.config import HTTP_CODES

from .egress import send_data
from .health import health_check


def stat_routes(app: Flask):
    """Sets the health route of the application

    Args:
        app (Flask): [Flask library]

    """
    @app.route('/health', methods=["GET"])
    def health():
        return health_check(), HTTP_CODES['OK']


def main_routes(app: Flask):
    """Sets the main application routes

    Args:
        app (Flask): [Flask library]
    """
    @app.route('/', methods=["POST"])
    def handle():
        received_data = request.get_json(force=True)

        sent = send_data(received_data)
        if sent:
            return "SUCCESS", HTTP_CODES['OK']
        app.logger.error("Error while transfering")
        return "ERROR while transfering", HTTP_CODES['INTERNAL_SERVER_ERROR']
