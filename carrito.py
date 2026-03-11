# La clase Carrito guarda los productos que el cliente quiere comprar

from excepciones import CantidadInvalidaError

class Carrito:
    """Representa el carrito de compras del cliente."""

    def __init__(self):
        # Cada item es un dict con el producto y la cantidad
        self.__items = []

    def agregar_producto(self, producto, cantidad):
        """Agrega un producto al carrito. Si ya existe, suma la cantidad."""
        if cantidad <= 0:
            raise CantidadInvalidaError(cantidad)

        # Reviso si el producto ya está en el carrito
        for item in self.__items:
            if item["producto"].get_id() == producto.get_id():
                item["cantidad"] += cantidad
                return

        # Si no estaba, lo agrego como item nuevo
        self.__items.append({"producto": producto, "cantidad": cantidad})

    def get_items(self):
        """Retorna la lista de items del carrito."""
        return self.__items

    def calcular_total(self):
        """Calcula y retorna el total a pagar."""
        total = 0
        for item in self.__items:
            total += item["producto"].get_precio() * item["cantidad"]
        return total

    def esta_vacio(self):
        """Retorna True si el carrito no tiene productos."""
        return len(self.__items) == 0

    def vaciar(self):
        """Vacía el carrito completamente."""
        self.__items = []