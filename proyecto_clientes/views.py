from models import Cliente
from shared.json_manager import GestorJSON

# Crear un gestor para el archivo de clientes
gestor = GestorJSON('data/clientes.json')

# ===== CREATE (Crear) =====

def crear_cliente(nombre, apellido, email, telefono, direccion):
    # Crea un nuevo cliente y lo guarda en JSON
    try:
        # Leer clientes existentes
        clientes_data = gestor.leer()
        
        # Calcular el siguiente ID
        if clientes_data:
            siguiente_id = max(c['id'] for c in clientes_data) + 1
        else:
            siguiente_id = 1
        
        # Crear el objeto Cliente
        cliente = Cliente(siguiente_id, nombre, apellido, email, telefono, direccion)
        
        # Convertir a diccionario
        datos_cliente = cliente.a_diccionario()
        
        # Agregar a la lista
        clientes_data.append(datos_cliente)
        
        # Guardar en JSON usando el gestor
        gestor.guardar(clientes_data)
        
        return True, f"Cliente {cliente.obtener_nombre_completo()} creado"
    
    except Exception as e:
        return False, f"Error: {str(e)}"

# ===== READ (Leer) =====

def obtener_todos():
    # Obtiene todos los clientes
    datos = gestor.leer()
    clientes = []
    
    for dato in datos:
        cliente = Cliente(
            dato['id'],
            dato['nombre'],
            dato['apellido'],
            dato['email'],
            dato['telefono'],
            dato['direccion']
        )
        clientes.append(cliente)
    
    return clientes

def obtener_cliente(id):
    # Obtiene un cliente por ID
    clientes = obtener_todos()
    for cliente in clientes:
        if cliente.id == id:
            return cliente
    return None

def buscar_clientes(termino):
    # Busca clientes por nombre, email o teléfono
    clientes = obtener_todos()
    resultados = []
    termino = termino.lower()
    
    for cliente in clientes:
        if (termino in cliente.nombre.lower() or
            termino in cliente.apellido.lower() or
            termino in cliente.email.lower() or
            termino in cliente.telefono):
            resultados.append(cliente)
    
    return resultados

# ===== UPDATE (Actualizar) =====

def actualizar_cliente(id, nombre=None, apellido=None, email=None, telefono=None, direccion=None):
    # Actualiza un cliente
    cliente = obtener_cliente(id)
    
    if not cliente:
        return False, f"Cliente con ID {id} no encontrado"
    
    # Actualizar solo los campos que se proporcionan
    if nombre:
        cliente.nombre = nombre
    if apellido:
        cliente.apellido = apellido
    if email:
        cliente.email = email
    if telefono:
        cliente.telefono = telefono
    if direccion:
        cliente.direccion = direccion
    
    # Guardar cambios
    clientes_data = gestor.leer()
    for i, dato in enumerate(clientes_data):
        if dato['id'] == id:
            clientes_data[i] = cliente.a_diccionario()
            break
    
    gestor.guardar(clientes_data)
    return True, f"Cliente {cliente.obtener_nombre_completo()} actualizado"

# ===== DELETE (Eliminar) =====

def eliminar_cliente(id):
    # Elimina un cliente
    cliente = obtener_cliente(id)
    
    if not cliente:
        return False, f"Cliente con ID {id} no encontrado"
    
    # Filtrar: guardar todos excepto el que tiene este ID
    clientes_data = gestor.leer()
    clientes_data = [c for c in clientes_data if c['id'] != id]
    
    gestor.guardar(clientes_data)
    return True, f"Cliente {cliente.obtener_nombre_completo()} eliminado"
            
            