import logging

from logging_config import setup_logging
from database import connect


setup_logging()

logger = logging.getLogger(__name__)

def main():

    logger.info("Aplicación iniciada")

    connect()

    logger.info("Aplicación finalizada")


if __name__ == "__main__":
    main()
