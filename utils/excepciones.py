# ============================================================
# ARCHIVO: excepciones.py
# Este archivo contiene las excepciones personalizadas
# del sistema.
# Las excepciones sirven para controlar errores específicos
# y evitar que el programa se cierre inesperadamente.
# ============================================================


# Clase principal de errores del sistema.
class ErrorSistema(Exception):
    pass


# Error utilizado cuando un cliente tiene datos inválidos.
class ClienteInvalidoError(ErrorSistema):
    pass


# Error utilizado cuando una reserva presenta problemas.
class ReservaError(ErrorSistema):
    pass


# Error utilizado cuando un servicio no está disponible.
class ServicioNoDisponibleError(ErrorSistema):
    pass