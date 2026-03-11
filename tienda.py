# Acá se coordina todo el programa

from catalogo import Catalogo
from admin import Admin
from cliente import Cliente
from producto import Producto
from excepciones import ProductoNoEncontradoError, CantidadInvalidaError
from datetime import datetime

# Los mismos colores del módulo 3 para mantener el hilo de los portafolios
VERDE_OSCURO   = "\033[32m"
VERDE_AMARILLO = "\033[33m"
MORADO         = "\033[35m"
AZUL           = "\033[34m"
NARANJO        = "\033[38;5;208m"
ROJO           = "\033[31m"
NEGRITA        = "\033[1m"
RESET          = "\033[0m"

class Tienda:
    """Coordina la ejecución del ecommerce y los menús por rol."""

    def __init__(self):
        # Al iniciar cargo el catálogo y dejo el usuario vacío
        self.__catalogo = Catalogo()
        self.__usuario = None
    
    def iniciar(self):
        """Inicio: pregunta si eres Admin o Cliente y lanza el menú."""
        print(f"\n{NEGRITA}🎾 Bienvenido a El Rincón del Tenis 🎾{RESET}")

        while True:
            print(f"\n¿Con qué rol deseas ingresar?")
            print(f"{VERDE_OSCURO}1) ADMIN{RESET}")
            print(f"{AZUL}2) CLIENTE{RESET}")
            print(f"{ROJO}0) Salir{RESET}")

            opcion = input("\nElige una opción: ").strip()

            if opcion == "1":
                nombre = input("Ingresa tu nombre: ").strip()
                self.__usuario = Admin(nombre)
                self.__menu_admin()
            elif opcion == "2":
                nombre = input("Ingresa tu nombre: ").strip()
                self.__usuario = Cliente(nombre)
                self.__menu_cliente()
            elif opcion == "0":
                print(f"\n{ROJO}Estas saliendo del programa...{RESET}\n")
                break
            else:
                print(f"{ROJO}Opción inválida, por favor ingresa una opción valida{RESET}")

    def __menu_admin(self): # el "__" es para privacidad
        """Menú con las opciones para el Admin."""
        while True:
            print(f"\n{NEGRITA} Menú ADMIN ({self.__usuario.get_nombre()}) {RESET}")
            print(f"{VERDE_OSCURO}1) Listar productos{RESET}")
            print(f"{VERDE_AMARILLO}2) Crear producto{RESET}")
            print(f"{MORADO}3) Actualizar producto{RESET}")
            print(f"{NARANJO}4) Eliminar producto{RESET}")
            print(f"{AZUL}5) Guardar catálogo en archivo{RESET}")
            print(f"{ROJO}0) Volver{RESET}")

            opcion = input("\nElige una opción: ").strip()

            if opcion == "1":
                self.__listar_productos()
            elif opcion == "2":
                self.__crear_producto()
            elif opcion == "3":
                self.__actualizar_producto()
            elif opcion == "4":
                self.__eliminar_producto()
            elif opcion == "5":
                self.__guardar_catalogo()
            elif opcion == "0":
                break
            else:
                print(f"{ROJO}Opción inválida{RESET}")

    def __menu_cliente(self):
        """Menú con las opciones para el Cliente."""
        carrito = self.__usuario.get_carrito() # para mas comodidad

        while True:
            print(f"\n{NEGRITA} Menú CLIENTE ({self.__usuario.get_nombre()}) {RESET}")
            print(f"{VERDE_OSCURO}1) Ver catálogo{RESET}")
            print(f"{VERDE_AMARILLO}2) Buscar producto{RESET}")
            print(f"{MORADO}3) Agregar al carrito{RESET}")
            print(f"{AZUL}4) Ver carrito y total{RESET}")
            print(f"{NARANJO}5) Confirmar compra{RESET}")
            print(f"{MORADO}6) Vaciar carrito{RESET}")
            print(f"{ROJO}0) Volver{RESET}")

            opcion = input("\nElige una opción: ").strip()

            if opcion == "1":
                self.__listar_productos()
            elif opcion == "2":
                self.__buscar_producto()
            elif opcion == "3":
                self.__agregar_al_carrito(carrito)
            elif opcion == "4":
                self.__ver_carrito(carrito)
            elif opcion == "5":
                self.__confirmar_compra(carrito)
            elif opcion == "6":
                self.__vaciar_carrito(carrito)
            elif opcion == "0":
                break
            else:
                print(f"{ROJO}Opción inválida{RESET}")

    # Ahora hare las funciones del ADMIN y las compartidas
    def __listar_productos(self):
        """Muestra todos los productos del catálogo."""
        productos = self.__catalogo.listar_productos()
        print(f"\n{NEGRITA} Catálogo de productos {RESET}")
        for producto in productos:
            print(f"{VERDE_OSCURO}{producto}{RESET}")

    def __buscar_producto(self):
        """Busca productos por nombre o categoría."""
        texto = input("\n¿Qué deseas buscar? ").strip()
        resultados = self.__catalogo.buscar_por_texto(texto)

        if not resultados:
            print(f"{ROJO}No se encontraron productos con '{texto}'{RESET}")
            return

        print(f"\n{NEGRITA}Resultados:{RESET}")
        for producto in resultados:
            print(f"{VERDE_AMARILLO}{producto}{RESET}")

    def __crear_producto(self):
        """Pide los datos y crea un producto nuevo en el catálogo."""
        print(f"\n{NEGRITA} Crear producto {RESET}")
        try:
            nombre = input("Nombre: ").strip()
            categoria = input("Categoría: ").strip()
            precio = int(input("Precio: "))

            # El id lo calcula el catálogo solo
            nuevo_id = self.__catalogo.get_siguiente_id()
            producto = Producto(nuevo_id, nombre, categoria, precio)
            self.__catalogo.agregar_producto(producto)
            print(f"{VERDE_OSCURO}✅ Producto '{nombre}' agregado con id {nuevo_id}{RESET}")

        except CantidadInvalidaError as e:
            print(f"{ROJO}Error: {e}{RESET}")
        except ValueError:
            print(f"{ROJO}El precio debe ser un número entero{RESET}")

    def __actualizar_producto(self):
        """Actualiza los datos de un producto existente."""
        print(f"\n{NEGRITA} Actualizar producto {RESET}")
        try:
            id_producto = int(input("ID del producto a actualizar: "))

            # Muestro el producto actual antes de editar
            producto = self.__catalogo.buscar_por_id(id_producto)
            print(f"Producto actual: {producto}")

            # Solo actualizo los campos que el admin quiera cambiar
            nombre = input("Nuevo nombre (Enter para dejar igual): ").strip()
            categoria = input("Nueva categoría (Enter para dejar igual): ").strip()
            precio_str = input("Nuevo precio (Enter para dejar igual): ").strip()

            precio = int(precio_str) if precio_str else None

            self.__catalogo.actualizar_producto(
                id_producto,
                nombre or None,
                categoria or None,
                precio
            )
            print(f"{VERDE_OSCURO}✅ Producto actualizado correctamente{RESET}")

        except ProductoNoEncontradoError as e:
            print(f"{ROJO}Error: {e}{RESET}")
        except CantidadInvalidaError as e:
            print(f"{ROJO}Error: {e}{RESET}")
        except ValueError:
            print(f"{ROJO}El precio debe ser un número entero{RESET}")

    def __eliminar_producto(self):
        """Elimina un producto del catálogo por su id."""
        print(f"\n{NEGRITA}--- Eliminar producto ---{RESET}")
        try:
            id_producto = int(input("ID del producto a eliminar: "))
            producto = self.__catalogo.buscar_por_id(id_producto)

            while True:
                confirmar = input(f"¿Seguro que quieres eliminar '{producto.get_nombre()}'? (s/n): ").strip().lower()
                if confirmar == "s":
                    self.__catalogo.eliminar_producto(id_producto)
                    print(f"{VERDE_OSCURO}✅ Producto eliminado correctamente{RESET}")
                    break
                elif confirmar == "n":
                    print(f"{NARANJO}Eliminación cancelada{RESET}")
                    break
                else:
                    print(f"{ROJO}Responde solo 's' o 'n'{RESET}")

        except ProductoNoEncontradoError as e:
            print(f"{ROJO}Error: {e}{RESET}")
        except ValueError:
            print(f"{ROJO}El ID debe ser un número entero{RESET}")

    # Ahora hare las funciones del CLIENTE y archivos
    def __agregar_al_carrito(self, carrito):
        """Agrega un producto al carrito del cliente."""
        print(f"\n{NEGRITA} Agregar al carrito {RESET}")
        try:
            id_producto = int(input("ID del producto: "))
            cantidad = int(input("Cantidad: "))

            producto = self.__catalogo.buscar_por_id(id_producto)
            carrito.agregar_producto(producto, cantidad)
            print(f"{MORADO}✅ '{producto.get_nombre()}' x{cantidad} agregado al carrito{RESET}")

        except ProductoNoEncontradoError as e:
            print(f"{ROJO}Error: {e}{RESET}")
        except CantidadInvalidaError as e:
            print(f"{ROJO}Error: {e}{RESET}")
        except ValueError:
            print(f"{ROJO}El ID y la cantidad deben ser números enteros{RESET}")

    def __ver_carrito(self, carrito):
        """Muestra los items del carrito y el total."""
        print(f"\n{NEGRITA}--- Tu carrito ---{RESET}")

        if carrito.esta_vacio():
            print(f"{NARANJO}El carrito está vacío{RESET}")
            return

        for item in carrito.get_items():
            producto = item["producto"]
            cantidad = item["cantidad"]
            subtotal = producto.get_precio() * cantidad
            print(f"{AZUL}{producto.get_nombre()} x{cantidad} → ${subtotal:,.0f}{RESET}")

        print(f"\n{NEGRITA}Total: ${carrito.calcular_total():,.0f}{RESET}")

    def __confirmar_compra(self, carrito):
        """Confirma la compra, guarda en ordenes.txt y vacía el carrito."""
        print(f"\n{NEGRITA}--- Confirmar compra ---{RESET}")

        if carrito.esta_vacio():
            print(f"{ROJO}No puedes confirmar una compra con el carrito vacío{RESET}")
            return

        self.__ver_carrito(carrito)

        while True:
            confirmar = input("\n¿Confirmas la compra? (s/n): ").strip().lower()
            if confirmar == "s":
                 # Guardo la orden en el archivo
                self.__guardar_orden(carrito)
                carrito.vaciar()
                print(f"{VERDE_OSCURO}✅ Compra confirmada. ¡Gracias por tu compra!{RESET}")
                break
            elif confirmar == "n":
                print(f"{NARANJO}Compra cancelada{RESET}")
                break
            else:
                print(f"{ROJO}Responde solo 's' o 'n'{RESET}")


    def __vaciar_carrito(self, carrito):
        """Vacía el carrito previa confirmación del usuario."""
        if carrito.esta_vacio():
            print(f"{NARANJO}El carrito ya está vacío{RESET}")
            return

        while True:
            confirmar = input("¿Seguro que quieres vaciar el carrito? (s/n): ").strip().lower()
            if confirmar == "s":
                carrito.vaciar()
                print(f"{MORADO}✅ Carrito vaciado{RESET}")
                break
            elif confirmar == "n":
                print(f"{NARANJO}Operación cancelada{RESET}")
                break
            else:
                print(f"{ROJO}Responde solo 's' o 'n'{RESET}")

    def __guardar_orden(self, carrito):
        """Guarda la orden en ordenes.txt con fecha y hora."""
        try:
            fecha = datetime.now().strftime("%Y-%m-%d %H:%M")
            with open("ordenes.txt", "a", encoding="utf-8") as archivo:
                archivo.write(f"\n=== Orden {fecha} — {self.__usuario.get_nombre()} ===\n")
                for item in carrito.get_items():
                    producto = item["producto"]
                    cantidad = item["cantidad"]
                    subtotal = producto.get_precio() * cantidad
                    archivo.write(f"{producto.get_nombre()} x{cantidad} → ${subtotal:,.0f}\n")
                archivo.write(f"Total: ${carrito.calcular_total():,.0f}\n")

        except OSError as e:
            print(f"{ROJO}No se pudo guardar la orden: {e}{RESET}")

    def __guardar_catalogo(self):
        """Guarda el catálogo actual en catalogo.txt."""
        try:
            with open("catalogo.txt", "w", encoding="utf-8") as archivo:
                for producto in self.__catalogo.listar_productos():
                    archivo.write(
                        f"{producto.get_id()}|{producto.get_nombre()}|"
                        f"{producto.get_categoria()}|{producto.get_precio()}\n"
                    )
            print(f"{AZUL}✅ Catálogo guardado en catalogo.txt{RESET}")

        except OSError as e:
            print(f"{ROJO}No se pudo guardar el catálogo: {e}{RESET}")

    