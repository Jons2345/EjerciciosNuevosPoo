import json
import os

class GestorJSON:
    # Esta clase maneja los archivos JSON
    # Recibe: la ruta del archivo (ej: 'data/clientes.json')
    
    def __init__(self, ruta):
        # Constructor: se ejecuta cuando creamos un GestorJSON
        self.ruta = ruta
        
        # Crear la carpeta si no existe
        carpeta = os.path.dirname(ruta)
        if carpeta and not os.path.exists(carpeta):
            os.makedirs(carpeta)
    
    def leer(self):
        # Lee todos los datos del archivo JSON
        # Retorna: lista de diccionarios
        
        if not os.path.exists(self.ruta):
            return []
        
        try:
            with open(self.ruta, 'r') as archivo:
                datos = json.load(archivo)
                return datos
        except:
            return []
    
    def guardar(self, datos):
        # Guarda datos en el archivo JSON
        # Recibe: datos (lista de diccionarios)
        
        try:
            with open(self.ruta, 'w') as archivo:
                json.dump(datos, archivo, ensure_ascii=False, indent=2)
            return True
        except:
            return False
            