
# Clase Producto
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Getters
    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio 
    
    # Setters
    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    def __str__(self):  
        return f"ID: {self.id} | Nombre: {self.nombre} | Cantidad: {self.cantidad} | Precio: ${self.precio:.2f}"


# Clase Inventario
class Inventario:
    def __init__(self):
        self.productos = []

    def añadir_producto(self, producto): 
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print(" Error: El ID ya existe. No se puede añadir el producto.")
                return
        self.productos.append(producto)
        print("Producto añadido correctamente.")

    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)   # corregido
                print(" Producto eliminado correctamente.")
                return
        print(" No se encontró un producto con ese ID.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        for p in self.productos:
            if p.get_id() == id_producto:
                if cantidad is not None:
                    p.set_cantidad(cantidad)
                if precio is not None:
                    p.set_precio(precio)
                print(" Producto actualizado correctamente.") 
                return
        print(" No se encontró un producto con ese ID.")

    def buscar_por_nombre(self, nombre):
        resultados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]  
        if resultados:
            print(" Resultados de búsqueda:")
            for p in resultados:
                print(p)
        else:
            print(" No se encontraron productos con ese nombre.")

    def mostrar_todos(self):
        if self.productos:
            print("Inventario completo:")
            for p in self.productos:
                print(p)
        else:
            print(" El inventario está vacío.")


# Interfaz del USUARIO
def menu():
    inventario = Inventario()

    # Inventario inicial (cosméticos)
    inventario.añadir_producto(Producto("C001", "Labial mate rojo", 20, 5.00))
    inventario.añadir_producto(Producto("C002", "Base Líquida Tono Natural", 15, 22.75))
    inventario.añadir_producto(Producto("C003", "Máscara de pestañas base de agua", 25, 7.99))
    inventario.añadir_producto(Producto("C004", "Polvo Compacto", 18, 10.90))
    inventario.añadir_producto(Producto("C005", "Rubor líquido en barra", 12, 6.99))

    while True:
        print("\n=== Menú de Inventario (COSMÉTICOS) ===")
        print("1. Añadir Producto")
        print("2. Eliminar Producto")
        print("3. Actualizar Producto")
        print("4. Buscar Producto por nombre")
        print("5. Mostrar todos los Productos")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            id_producto = input("Ingrese ID: ")
            nombre = input("Ingrese nombre: ")
            cantidad = int(input("Ingrese cantidad: "))  
            precio = float(input("Ingrese precio: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == "2":
            id_producto = input("Ingrese ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("Ingrese ID del producto a actualizar: ")        
            cantidad = input("Nueva cantidad (dejar vacío si no desea cambiar): ")
            precio = input("Nuevo precio (dejar vacío si no desea cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id_producto, cantidad, precio)

        elif opcion == "4":
            nombre = input("Ingrese nombre o parte del nombre a buscar: ")    
            inventario.buscar_por_nombre(nombre)

        elif opcion == "5":
            inventario.mostrar_todos()

        elif opcion == "6":
            print(" Saliendo del sistema....")
            break
        
        else:
            print("❌ Opción inválida, intente de nuevo.")


# Ejecución principal
if __name__ == "__main__":
    menu()





    
                                 

           
