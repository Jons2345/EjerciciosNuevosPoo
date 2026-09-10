import json

class Cliente:
    # CLASE: Representa un cliente
    # Un cliente tiene: id, nombre, apellido, email, teléfono, dirección
    
    def __init__(self, id, nombre, apellido, email, telefono, direccion):
        # CONSTRUCTOR: Se ejecuta al crear un nuevo cliente
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono
        self.direccion = direccion
    
    def obtener_nombre_completo(self):
        # Retorna: "Nombre Apellido"
        return f"{self.nombre} {self.apellido}"
    
    def a_diccionario(self):
        # Convierte el cliente a un diccionario
        # Esto es útil para procesar los datos
        datos = {
            'id': self.id,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'email': self.email,
            'telefono': self.telefono,
            'direccion': self.direccion
        }
        return datos
    
    def a_json(self):
        # Convierte el cliente a JSON (texto)
        # El GestorJSON usará esto para guardar
        return json.dumps(self.a_diccionario(), ensure_ascii=False)
    
    def __str__(self):
        # Cómo se ve el cliente cuando lo imprimimos
        return f"[{self.id}] {self.obtener_nombre_completo()} - {self.email}"


class Estudiante:
    # CLASE: Representa un estudiante
    # Un estudiante tiene: id, nombre, apellido, email, carnet, notas
    
    def __init__(self, id, nombre, apellido, email, carnet):
        # CONSTRUCTOR: Se ejecuta al crear un nuevo estudiante
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.carnet = carnet  # Ej: EST2024001
        self.notas = {}  # Diccionario: {"Matemática": [18, 19], "Español": [17]}
    
    def obtener_nombre_completo(self):
        # Retorna: "Nombre Apellido"
        return f"{self.nombre} {self.apellido}"
    
    def agregar_nota(self, materia, nota):
        # Agrega una nota a una materia
        if materia not in self.notas:
            self.notas[materia] = []
        self.notas[materia].append(nota)
    
    def obtener_promedio(self):
        # Calcula el promedio de todas las notas
        todas_notas = []
        for materia in self.notas:
            todas_notas.extend(self.notas[materia])
        
        if not todas_notas:
            return 0
        
        promedio = sum(todas_notas) / len(todas_notas)
        return round(promedio, 2)
    
    def a_diccionario(self):
        # Convierte el estudiante a diccionario
        datos = {
            'id': self.id,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'email': self.email,
            'carnet': self.carnet,
            'notas': self.notas
        }
        return datos
    
    def a_json(self):
        # Convierte el estudiante a JSON
        return json.dumps(self.a_diccionario(), ensure_ascii=False)
    
    def __str__(self):
        # Cómo se ve el estudiante cuando lo imprimimos
        promedio = self.obtener_promedio()
        return f"[{self.carnet}] {self.obtener_nombre_completo()} - Promedio: {promedio}"
            