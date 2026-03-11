# Creo la clase Cliente que hereda de la clase Usuario 

from usuario import Usuario
from carrito import Carrito

class Cliente(Usuario):
    """Usuario que puede navegar el catálogo y realizar compras."""

    def __init__(self, nombre):
        # Le paso el rol fijo "CLIENTE" a la clase padre
        super().__init__(nombre, "CLIENTE")
        # Cada cliente tiene su propio carrito
        self.__carrito = Carrito()

    def get_carrito(self):
        return self.__carrito