La aplicación
-------------

Configura el logging.

Inicia el programa.

Llama a la función connect().

Registra el resultado de la conexión.

Finaliza la aplicación.


#################################################################
python logging learning
#################################################################

logging = Librería estándar para registrar evento.
logging está diseñado para registrar y controlar eventos de una aplicación. Ayuda a depurar errore.

Niveles = DEBUG, INFO, WARNING, ERROR y CRITICAL.

Logger = Objeto que crea mensajes de registro y controla que mensajes puede procesar el logger.
------
Jerarquia de loggers: Los loggers tienen una estructura jerárquica basada en sus nombres.
Los mensajes de un logger hijo pueden propagarse al logger padre y a los handlers asociados, según la configuración
logger = logging.getLogger() ===> en login_config.py , root logger
logger = logging.getLogger(__name__) ==> en resto py files

Handler = Define el destino del registro.
-------
file_handler = logging.FileHandler("app.log")
file_handler.setLevel(logging.DEBUG)

Formatter = Define el formato del mensaje.
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
console_handler.setFormatter(formatter)

logger.exception() = Registra una excepción con su traceback dentro de un bloque except.

HANDLER
-------
Un handler es el componente que recibe los registros y los dirige a un destino.

Los handlers más utilizados son:


StreamHandler
Envía registros a un flujo, como la consola
FileHandler
Guarda registros en un archivo
RotatingFileHandler
Rota archivos según su tamaño
TimedRotatingFileHandler
Rota archivos según el tiempo



Buenas prácticas
----------------

1. Usa logging.getLogger(__name__).

Facilita identificar el módulo que genera el registro.

2. Configura logging en un punto central. Separar la config del logging del resto de la logica.

Evita crear handlers repetidos en cada función.

3. Usa niveles apropiados.

DEBUG para diagnóstico detallado, INFO para eventos normales y ERROR para fallos.

4. No registres información sensible.

Evita contraseñas, tokens, claves API y datos personales innecesarios.

5. Utiliza logger.exception() cuando corresponda.

Es útil para conservar el traceback de errores manejados.

6. Si la app va a correr mucho tiempo usa un RotatingFileHandler

import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger("mi_app")
logger.setLevel(logging.INFO)

handler = RotatingFileHandler(
    "app.log",
    maxBytes=10000, # cuando el archivo log llega 10 Megas, entonces rota
    backupCount=3 # guarda app.log , .log.1, .log.2, .log.3
)

formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)

handler.setFormatter(formatter)

logger.addHandler(handler)

logger.info("Aplicación iniciada")
7. Evitar duplicidad de logs
configurar_logging()
...
configurar_logging()

Por eso se anade esto en el logging_config.py:
    if logger.handlers:
        return