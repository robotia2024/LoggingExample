import logging
import sys


def setup_logging():
    # 1. Crear logger
    logger = logging.getLogger() #logger raiz <sin __name__> - Lo correcto es configurar el root una sola vez
    # 2. Nivel mínimo del logger
    logger.setLevel(logging.DEBUG)

    # Evitar duplicar handlers al volver a configurar
    if logger.handlers:
        return

    # 3. Handler para consola
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)

    # 4. Handler para archivo
    file_handler = logging.FileHandler("app.log")
    file_handler.setLevel(logging.DEBUG)

    # 5. Formatter
    formatter = logging.Formatter(
        "%(asctime)s | "
        "%(levelname)s | "
        "%(name)s | "
        "%(funcName)s:%(lineno)d | "
        "%(message)s"
    )
    # 6. Aplicar formatter a los handlers
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)
    # 7. Añadir handlers al logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    # 8. Crear mensajes
    logger.info("Logging setup hecho")