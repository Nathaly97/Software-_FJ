# ============================================================
# ARCHIVO: cliente.py
# Este archivo contiene la clase Cliente.
# La clase Cliente hereda de la clase Persona.
# ============================================================


# Importación de la clase Persona.
from models.persona import Persona

# Importación de excepciones personalizadas.
from utils.excepciones import ClienteInvalidoError


# Clase Cliente.
class Cliente(Persona):

    # Constructor de la clase.
    def __init__(self, nombre, email):

        # Se llama al constructor de Persona.
        super().__init__(nombre)

        # Encapsulación:
        # El atributo email será privado.
        self.__email = email

        # Se validan los datos.
        self.validar_datos()

    # Método encargado de validar datos.
    def validar_datos(self):

        # Validar longitud del nombre.
        if len(self.nombre) < 3:
            raise ClienteInvalidoError(
                "El nombre debe tener mínimo 3 caracteres."
            )

        # Validar correo electrónico.
        if "@" not in self.__email:
            raise ClienteInvalidoError(
                "Correo electrónico inválido."
            )

    # Método getter.
    def get_email(self):
        return self.__email

    # Método obligatorio heredado.
    def mostrar_informacion(self):

        return f"Cliente: {self.nombre} - Email: {self.__email}"