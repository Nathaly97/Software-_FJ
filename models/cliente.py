# ============================================================
# ARCHIVO: cliente.py
# 
# Este archivo contiene la clase Cliente.
#
# La clase Cliente hereda de la clase Persona
# y permite almacenar y validar información
# de los clientes del sistema.
# ============================================================


# ============================================================
# IMPORTACIÓN DE CLASES Y EXCEPCIONES
# ============================================================

# Se importa la clase Persona.
from models.persona import Persona

# Se importa la excepción personalizada.
from utils.excepciones import ClienteInvalidoError


# ============================================================
# CLASE CLIENTE
# ============================================================

# La clase Cliente hereda de Persona.
class Cliente(Persona):

    # ========================================================
    # CONSTRUCTOR
    # --------------------------------------------------------
    # Este método se ejecuta automáticamente al crear
    # un nuevo cliente.
    # ========================================================

    def __init__(self, nombre, email):

        # Se llama al constructor de la clase padre.
        super().__init__(nombre)

        # Encapsulación:
        # El atributo email será privado.
        self.__email = email

        # Se validan los datos del cliente.
        self.validar_datos()


    # ========================================================
    # MÉTODO VALIDAR DATOS
    # --------------------------------------------------------
    # Este método verifica que la información ingresada
    # por el usuario sea correcta.
    # ========================================================

    def validar_datos(self):

        # ----------------------------------------------------
        # VALIDAR NOMBRE
        # ----------------------------------------------------

        # Verifica que el nombre tenga al menos 3 caracteres.
        if len(self.nombre) < 3:

            # Se genera una excepción personalizada.
            raise ClienteInvalidoError(
                "El nombre debe tener mínimo 3 caracteres."
            )

        # ----------------------------------------------------
        # VALIDAR CORREO ELECTRÓNICO
        # ----------------------------------------------------

        try:

            # Verifica si el correo contiene "@"
            if "@" not in self.__email:

                # Se genera un error interno.
                raise ValueError(
                    "Formato de correo incorrecto."
                )

        # ----------------------------------------------------
        # ENCADENAMIENTO DE EXCEPCIONES
        # ----------------------------------------------------

        except ValueError as error:

            # Se genera una excepción personalizada
            # tomando como base el error original.
            raise ClienteInvalidoError(
                "Correo electrónico inválido."
            ) from error


    # ========================================================
    # MÉTODO GETTER
    # --------------------------------------------------------
    # Permite obtener el email del cliente.
    # ========================================================

    def get_email(self):

        return self.__email


    # ========================================================
    # MÉTODO MOSTRAR INFORMACIÓN
    # --------------------------------------------------------
    # Este método devuelve la información del cliente.
    # ========================================================

    def mostrar_informacion(self):

        return f"Cliente: {self.nombre} - Email: {self.__email}"