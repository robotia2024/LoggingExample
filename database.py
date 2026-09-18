import logging

logger = logging.getLogger(__name__)


def connect():

    logger.info("Intentando conectar a la base de datos")

    try:
        # Simulación de conexión
        connection_successful = True

        if not connection_successful:
            raise ConnectionError("No se pudo conectar")

        logger.info("Conexión exitosa")

    except ConnectionError:
        logger.exception("Error en la conexión") #esto explica el error y se imprime antes del traceback