# ============================================================
# ARCHIVO: logger.py
# ------------------------------------------------------------
# Este archivo se encarga de registrar eventos y errores
# dentro del sistema.
#
# Todos los mensajes se almacenan en el archivo logs.txt
# ============================================================


# Se importa datetime para registrar fecha y hora.
from datetime import datetime


# Función encargada de guardar logs.
def registrar_log(mensaje):

    # Se abre el archivo logs.txt en modo agregar.
    with open("logs.txt", "a", encoding="utf-8") as archivo:

        # Se escribe la fecha y el mensaje recibido.
        archivo.write(f"{datetime.now()} - {mensaje}\n")