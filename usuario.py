# Clase base para los dos tipos de usuario del sistema

class Usuario:
    """Clase base que representa un usuario del sistema."""

    def __init__(self, nombre, rol):
        self.__nombre = nombre
        self.__rol = rol

    def get_nombre(self):
        return self.__nombre

    def get_rol(self):
        return self.__rol

    def __str__(self):
        return f"{self.__nombre} ({self.__rol})"