# ============================================================
# ARCHIVO: persona.py
# Este archivo contiene la clase abstracta Persona.
# Una clase abstracta funciona como plantilla para
# otras clases.
# ============================================================


# Se importa ABC y abstractmethod para crear clases abstractas.
from abc import ABC, abstractmethod


# Clase abstracta Persona.
class Persona(ABC):

    # Constructor de la clase.
    def __init__(self, nombre):

        # Guarda el nombre de la persona.
        self.nombre = nombre

    # Método abstracto obligatorio.
    @abstractmethod
    def mostrar_informacion(self):
        pass