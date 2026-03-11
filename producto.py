# Acá defino la clase que representa cada producto del catálogo
from excepciones import CantidadInvalidaError

class Producto:
    """Representa un producto del Rincón del Tenis."""

    def __init__(self, id_producto, nombre, categoria, precio):
        # Guardo los datos básicos de cada producto
        self.__id_producto = id_producto
        self.__nombre = nombre
        self.__categoria = categoria
        self.__precio = precio

    # Estos son los Getters
    def get_id(self):
        return self.__id_producto

    def get_nombre(self):
        return self.__nombre

    def get_categoria(self):
        return self.__categoria

    def get_precio(self):
        return self.__precio

    # Estos son los Setters con validacion incluida
    def set_nombre(self, nuevo_nombre):
        if nuevo_nombre.strip() == "":
            raise ValueError("El nombre no puede estar vacío")
        self.__nombre = nuevo_nombre

    def set_categoria(self, nueva_categoria):
        if nueva_categoria.strip() == "":
            raise ValueError("La categoría no puede estar vacía")
        self.__categoria = nueva_categoria

    def set_precio(self, nuevo_precio):
        if nuevo_precio <= 0:
            raise CantidadInvalidaError(nuevo_precio)
        self.__precio = nuevo_precio

    # Defino como se vera para nosotros los humanos
    def __str__(self):
        return (f"[{self.__id_producto}] {self.__nombre} "
                f"| {self.__categoria} "
                f"| ${self.__precio:,.0f}") # defino formato