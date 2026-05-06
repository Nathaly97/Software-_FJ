# ============================================================
# ARCHIVO: servicio.py
# Este archivo contiene la clase abstracta Servicio
# y las clases hijas del sistema.
# ============================================================


# Importación para clases abstractas.
from abc import ABC, abstractmethod


# Clase abstracta Servicio.
class Servicio(ABC):

    # Constructor de la clase.
    def __init__(self, nombre_servicio, precio_base):

        # Nombre del servicio.
        self.nombre_servicio = nombre_servicio

        # Precio base.
        self.precio_base = precio_base

    # Método abstracto para calcular costos.
    @abstractmethod
    def calcular_costo(self, horas):
        pass

    # Método abstracto para mostrar descripción.
    @abstractmethod
    def descripcion(self):
        pass


# ============================================================
# CLASE RESERVA DE SALA
# ============================================================

class ReservaSala(Servicio):

    # Método sobrescrito.
    def calcular_costo(self, horas):

        return self.precio_base * horas

    # Método sobrescrito.
    def descripcion(self):

        return "Servicio de reserva de salas."


# ============================================================
# CLASE ALQUILER DE EQUIPOS
# ============================================================

class AlquilerEquipo(Servicio):

    # Método sobrescrito.
    def calcular_costo(self, horas):

        # Se agrega un costo adicional.
        return (self.precio_base * horas) + 50

    # Método sobrescrito.
    def descripcion(self):

        return "Servicio de alquiler de equipos."


# ============================================================
# CLASE ASESORÍA
# ============================================================

class Asesoria(Servicio):

    # Método sobrescrito.
    def calcular_costo(self, horas):

        # Se agrega un incremento del 20%.
        return self.precio_base * horas * 1.20

    # Método sobrescrito.
    def descripcion(self):

        return "Servicio de asesoría especializada."