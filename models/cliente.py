from utils.excepciones import ClienteInvalidoError

class Cliente:
    def __init__(self, nombre, email):
        self.__nombre = nombre
        self.__email = email
        self.validar()

    def validar(self):
        if not self.__nombre or len(self.__nombre) < 3:
            raise ClienteInvalidoError("Nombre inválido")

        if "@" not in self.__email:
            raise ClienteInvalidoError("Email inválido")

    def get_nombre(self):
        return self.__nombre

    def get_email(self):
        return self.__email