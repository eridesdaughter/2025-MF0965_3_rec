class Producto:
    def __init__(self, codigo, nombre, precio):
        self.codigo = "PROD001", "PROD002"
        self.nombre = "Teclado Mecanico"
        self.precio = 75.50

    def __str__(self):
        msg = f"{self.codigo} {self.nombre} - {self.precio} €"

        return msg


def buscar_producto(inventario, codigo_buscar):
    for producto in inventario:
        print(producto)
    else:
        None


def mostrar_inventario(inventario):
    """
    COMPLETAR 4:
    Imprime por pantalla todos los productos que hay en 'inventario'.
    """
    print("\n--- INVENTARIO ACTUAL ---")
    for producto in inventario:
        print(producto)

    if not inventario:
        print("El inventario está vacío.")
    else:
        pass


def calcular_valor_total(inventario):
    precio_producto1 = 75.50
    precio_producto2 = 25.00

    valor_total = precio_producto1 + precio_producto2

    return valor_total


def main():
    inventario = [
        Producto("PROD001", "Teclado Mecánico", 75.50),
        Producto("PROD002", "Mouse Inalámbrico", 25.00)
    ]

    while True:
        print("\n===============================")
        print("  MENÚ DE GESTIÓN DE INVENTARIO")
        print("===============================")
        print("1. Mostrar inventario")
        print("2. Buscar producto")
        print("3. Calcular valor total del inventario")
        print("4. Salir")
        opcion = input("Seleccione una opción (1-4): ")

        if opcion == '1':
            mostrar_inventario(inventario)
        elif opcion == '2':
            codigo_buscar = input("Ingrese el código del producto a buscar: ")
            producto_encontrado = buscar_producto(inventario, codigo_buscar)
            if producto_encontrado is not None:
                print(f"Producto encontrado: ", ({producto_encontrado}))
            else:
                None
                print("No se encontró ningún producto con ese código")

            """
            COMPLETAR 6:
            Comprueba si 'producto_encontrado' es distinto de None.
            Si se encontró, imprime ">> Producto encontrado:" y luego el producto.
                     Si no, imprime ">> No se encontró ningún producto con ese código."
            """

        elif opcion == '3':
            valor_total = calcular_valor_total(inventario)
            print(f"\n>> El valor total del inventario es: {valor_total:.2f} €")
        elif opcion == '4':
            print("\nSaliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elija entre 1 y 4.")


if __name__ == "__main__":
    main()