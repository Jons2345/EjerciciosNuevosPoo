from shared.herramientas import (
    imprimir_titulo, imprimir_exito, imprimir_error, imprimir_info
)
from views import (
    crear_cliente, obtener_todos, obtener_cliente, buscar_clientes,
    actualizar_cliente, eliminar_cliente
)

def mostrar_menu():
    # Muestra el menú principal
    imprimir_titulo("SISTEMA DE GESTIÓN DE CLIENTES")
    print("  1. Crear nuevo cliente")
    print("  2. Ver todos los clientes")
    print("  3. Buscar cliente")
    print("  4. Ver cliente por ID")
    print("  5. Actualizar cliente")
    print("  6. Eliminar cliente")
    print("  7. Salir")
    imprimir_info("-" * 60)

def opcion_crear():
    # Opción 1: Crear cliente
    imprimir_titulo("CREAR NUEVO CLIENTE")
    
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    email = input("Email: ")
    telefono = input("Teléfono: ")
    direccion = input("Dirección: ")
    
    exito, mensaje = crear_cliente(nombre, apellido, email, telefono, direccion)
    
    if exito:
        imprimir_exito(mensaje)
    else:
        imprimir_error(mensaje)
    
    input("\nPresione Enter para continuar...")

def opcion_ver_todos():
    # Opción 2: Ver todos los clientes
    imprimir_titulo("LISTA DE CLIENTES")
    
    clientes = obtener_todos()
    
    if not clientes:
        imprimir_error("No hay clientes registrados")
    else:
        print(f"{'ID':<5} {'NOMBRE':<20} {'EMAIL':<30} {'TELÉFONO':<12}")
        print("-" * 70)
        
        for cliente in clientes:
            print(f"{cliente.id:<5} {cliente.obtener_nombre_completo():<20} {cliente.email:<30} {cliente.telefono:<12}")
        
        print("-" * 70)
        imprimir_info(f"Total: {len(clientes)} cliente(s)")
    
    input("\nPresione Enter para continuar...")

def opcion_buscar():
    # Opción 3: Buscar cliente
    imprimir_titulo("BUSCAR CLIENTE")
    
    termino = input("Ingrese nombre, email o teléfono: ")
    resultados = buscar_clientes(termino)
    
    if not resultados:
        imprimir_error(f"No se encontraron clientes")
    else:
        imprimir_info(f"Se encontraron {len(resultados)} cliente(s):\n")
        
        for cliente in resultados:
            print(f"ID: {cliente.id}")
            print(f"  Nombre: {cliente.obtener_nombre_completo()}")
            print(f"  Email: {cliente.email}")
            print(f"  Teléfono: {cliente.telefono}")
            print(f"  Dirección: {cliente.direccion}\n")
    
    input("Presione Enter para continuar...")

def opcion_ver_por_id():
    # Opción 4: Ver cliente por ID
    imprimir_titulo("BUSCAR POR ID")
    
    try:
        id = int(input("Ingrese ID del cliente: "))
        cliente = obtener_cliente(id)
        
        if not cliente:
            imprimir_error(f"Cliente con ID {id} no encontrado")
        else:
            imprimir_info("DATOS DEL CLIENTE:")
            print(f"  ID: {cliente.id}")
            print(f"  Nombre: {cliente.obtener_nombre_completo()}")
            print(f"  Email: {cliente.email}")
            print(f"  Teléfono: {cliente.telefono}")
            print(f"  Dirección: {cliente.direccion}")
    
    except ValueError:
        imprimir_error("El ID debe ser un número")
    
    input("\nPresione Enter para continuar...")

def opcion_actualizar():
    # Opción 5: Actualizar cliente
    imprimir_titulo("ACTUALIZAR CLIENTE")
    
    try:
        id = int(input("Ingrese ID del cliente: "))
        cliente = obtener_cliente(id)
        
        if not cliente:
            imprimir_error(f"Cliente con ID {id} no encontrado")
        else:
            imprimir_info(f"Cliente actual: {cliente.obtener_nombre_completo()}")
            print("Deje en blanco para no cambiar\n")
            
            nombre = input("Nuevo nombre (Enter para omitir): ")
            apellido = input("Nuevo apellido (Enter para omitir): ")
            email = input("Nuevo email (Enter para omitir): ")
            telefono = input("Nuevo teléfono (Enter para omitir): ")
            direccion = input("Nueva dirección (Enter para omitir): ")
            
            exito, mensaje = actualizar_cliente(
                id,
                nombre if nombre else None,
                apellido if apellido else None,
                email if email else None,
                telefono if telefono else None,
                direccion if direccion else None
            )
            
            if exito:
                imprimir_exito(mensaje)
            else:
                imprimir_error(mensaje)
    
    except ValueError:
        imprimir_error("El ID debe ser un número")
    
    input("\nPresione Enter para continuar...")

def opcion_eliminar():
    # Opción 6: Eliminar cliente
    imprimir_titulo("ELIMINAR CLIENTE")
    
    try:
        id = int(input("Ingrese ID del cliente: "))
        cliente = obtener_cliente(id)
        
        if not cliente:
            imprimir_error(f"Cliente con ID {id} no encontrado")
        else:
            imprimir_info(f"Cliente a eliminar: {cliente.obtener_nombre_completo()}")
            confirmar = input("¿Está seguro? (si/no): ")
            
            if confirmar.lower() == 'si':
                exito, mensaje = eliminar_cliente(id)
                if exito:
                    imprimir_exito(mensaje)
                else:
                    imprimir_error(mensaje)
            else:
                imprimir_info("Operación cancelada")
    
    except ValueError:
        imprimir_error("El ID debe ser un número")
    
    input("\nPresione Enter para continuar...")

def main():
    # LOOP PRINCIPAL del programa
    while True:
        mostrar_menu()
        
        opcion = input("Seleccione opción: ")
        
        if opcion == '1':
            opcion_crear()
        elif opcion == '2':
            opcion_ver_todos()
        elif opcion == '3':
            opcion_buscar()
        elif opcion == '4':
            opcion_ver_por_id()
        elif opcion == '5':
            opcion_actualizar()
        elif opcion == '6':
            opcion_eliminar()
        elif opcion == '7':
            imprimir_info("\n¡Hasta luego! 👋\n")
            break
        else:
            imprimir_error("Opción no válida")
            input("Presione Enter para continuar...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        imprimir_error("\n\n¡Programa interrumpido!\n")
            