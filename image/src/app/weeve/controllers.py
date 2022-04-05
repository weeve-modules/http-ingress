"""
All route entry points
"""
from flask import Flask, request

from app.config import HTTP_CODES

from .egress import send_data
from .health import health_check
from app.config import APPLICATION

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
        if APPLICATION['AUTHENTICATION_REQUIRED']=='yes' and APPLICATION['AUTHENTICATION_TOKEN']!='':
            request.headers.set({"Authorization": f"{APPLICATION['AUTHENTICATION_TOKEN']}"})
        if APPLICATION['AUTHENTICATION_API_KEY']!='':
            request.headers.set({'x-api-key': APPLICATION['AUTHENTICATION_API_KEY']})
        received_data = request.get_json(force=True)

        sent = send_data(received_data)
        if sent:
            return "SUCCESS", HTTP_CODES['OK']
        app.logger.error("Error while transfering")
        return "ERROR while transfering", HTTP_CODES['INTERNAL_SERVER_ERROR']
