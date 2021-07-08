"""Main app file"""
from logging import getLogger
from app import create_app
from app.config import WEEVE, APPLICATION, configure_logging


log = getLogger("main")


def main():
    """ Main app entry point"""
    configure_logging()
    log.info("%s Started", WEEVE["MODULE_NAME"])
    app = create_app()
    app.run(host=APPLICATION['HANDLER_HOST'], port=APPLICATION["HANDLER_PORT"])


if __name__ == "__main__":
    main()
