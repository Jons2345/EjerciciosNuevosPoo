##Escribe una función estadisticas(numeros) que reciba una lista de números y
# retorne un dict con: total, promedio, máximo, mínimo, cantidad de pares.

## ======== Analisis ======== ##
## Paso 1: Entender el problema: 
# Entrada: Se crea una lista de enteros
# Proceso: Se recorre una vez, se acumulan varios contenedores y se forma un dict
# Salida: Sale un diccionario con las estadisticas

## Paso 2: Bosquejo
# num [5, 7, 8, 6, 3]
# suma acumulada es = 5, 12, 20, 26, 29
# el valor maximo se actualiza si es mayor
# el valor minimo se actualiza si es menor
# en pares se incrementa el contador si n % 2 == 0

## Paso 3: Descubrir el patrón
# Me di cuenta que retornar un dict es más útil que retornar una tupla, aunque en Python 
# se tiene mas alternativas como sum(), max(), min(), que serian mas utiles para listas grandes,
# pero el objetivo es recorrer la lista una sola vez.

## Paso 4: Escribir el código

def estadisticas(numeros):
    if not numeros:
        return {"total": 0, "promedio": 0, "max": None, "min": None, "pares": 0}
    
    total = 0
    maximo = numeros[0]
    minimo = numeros[0]
    pares = 0
    
    for n in numeros:
        total += n
        if n > maximo: maximo = n
        if n < minimo: minimo = n
        if n % 2 == 0: pares += 1
        
    return {
        "total": total,
        "promedio": total / len(numeros),
        "max": maximo,
        "min": minimo,
        "pares": pares
    }


r = estadisticas([5, 7, 8, 6, 3])
print(r)
print(f"Promedio: {r['promedio']:.2f}")

    
## -------------------------------------------------------------------------------------------- ##
##Función contar_unicas(texto) que reciba una cadena y retorne 
# un dict {{ palabra: cantidad_de_apariciones }}. Ignorar mayúsculas y
# signos de puntuación básicos (.,;:!?).

## ======== Analisis ======== ##
## Paso 1: Entender el problema:
# Entrada: Se crea una cadena de texto para empezar a contar las palabras
# Proceso: se dividide en palabras, se limpia y se empieza a contar cada aparición
# Salida: Sale un diccionario con las palabras y frecuencias
 
## Paso 2: Bosquejo
# texto = "Joel lino estudia, Joel lino aprende"

# Se pasa a minúsculas
# Se quita los signos
# Se divide por espacios
#   palabras = ["Joel", "lino", "estudia", "Joel", "lino", "aprende"]
# Se cuenta las palabras y se guarda en un dict
#   "joel" aparece 2 veces
#   "lino" aparece 2 veces
#   "estudia" aparece 1 vez
#   "aprende" aparece 1 vez

## Paso 3: Descubrir el patrón
# la clave para contar cada elemento se utilizo un diccionario contador, donde la clave es la palabra y el valor es la cantidad de apariciones.
# para cumplir con los requisitos de ignorar mayúsculas y signos de puntuación, 
# se utilizo lower() y replace() para limpiar el texto antes de contar.
#  ademas se utilizo el get  que devuelve el valor actual o 0 si no existe,



## Paso 4: Escribir el código
def contar_unicas(texto):
    texto = texto.lower()
    for signo in ".,;:!?\"'()":
        texto = texto.replace(signo, "")

    frecuencias = {}
    for palabra in texto.split():
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1

    return frecuencias


texto = "Joel lino estudia, Joel lino aprende"
r = contar_unicas(texto)
for palabra, cant in r.items():
    print(f"{palabra}: {cant}")
    
## -------------------------------------------------------------------------------------------- ##    
##Función guardar_config(datos, archivo) y cargar_config(archivo). 
# Si el archivo no existe al cargar, retornar un dict vacío.

## ======== Analisis ======== ##
## Paso 1: Entender el problema: 
# Entrada: se crea un dict de configuración (para guardar) o una ruta de archivo (para cargar)
# Proceso: verificar si el archivo existe, leer/escribir en formato JSON
# Salida: en guardar_config escribe en disco y en cargar_config se retorna un dict

## Paso 2: Bosquejo
#cargar_config(archivo):
#    ¿el archivo existe? (os.path.exists)
#        NO -> retornar {}
#        SÍ -> abrir, leer JSON, retornar el dict

#guardar_config(datos, archivo):
#    abrir archivo en modo escritura
#    convertir el dict a JSON y escribirlo


## Paso 3: Descubrir el patrón
# se utiliza el os.path.exists() que es más explícito y fácil de leer que el try/except que se uso,
# se uso El patrón "cargar → modificar el dict en memoria → guardar" 
# que es exactamente cómo funcionan la mayoría de las apps con configuración persistente 

## Paso 4: Escribir el código
import json
import os
def guardar_config(datos, archivo):
    with open(archivo, 'w') as f:
        json.dump(datos, f)

def cargar_config(archivo):
    if not os.path.exists(archivo):
        return {}
    with open(archivo, 'r') as f:
        return json.load(f)
    
    
confi = cargar_config("config.json")
confi["usuario"] = "Joel"
confi["tema"] = "claro"
confi["idioma"] = "español"
guardar_config(confi, "config.json")


##Función sin_duplicados(lista) que retorne una lista nueva sin duplicados pero conservando el orden de la primera aparición.

## ======== Analisis ======== ##
## Paso 1: Entender el problema:
# Entrada: Se crea una lista de enteros
# Proceso: se recorrer una vez, se recuerda los elementos que se vieron, y solo se agrega los que no se vieron
# Salida:  sale como resultado final una lista nueva sin duplicados, respetando el orden original
 
## Paso 2: Bosquejo
#lista = [2, 5, 7, 8, 3, 5, 2, 9]

# Se hace un solo recorrido:
#  vistos = {}       (es un conjunto vacío)
#  resultado = []    (es una lista vacía)

#  2 -> no está en vistos -> agrego -> resultado: [2],         vistos: {2}
#  5 -> no está en vistos -> agrego -> resultado: [2,5],       vistos: {2,5}
#  7 -> no está en vistos -> agrego -> resultado: [2,5,7],     vistos: {2,5,7}
#  ...
#  Al final retorno resultado.

## Paso 3: Descubrir el patrón
# El set de vistos no es el resultado final, ya que es solo una estructura de apoyo para hacer la búsqueda de 
# elemento not in vistos en tiempo O(1) en vez de O(n) 

# El Separar "memoria de lo visto" de "acumulador de salida" es lo que permite lograr ambas cosas a la vez: eficiencia y orden.

## Paso 4: Escribir el código
def sin_duplicados(lista):
    vistos = set()
    resultado = []
    for elemento in lista:
        if elemento not in vistos:
            vistos.add(elemento)
            resultado.append(elemento)
    return resultado
   
print(sin_duplicados([2, 5, 7, 8, 3, 5, 2, 9]))
    

## En vez de una cascada if/elif, usa un dict donde la clave es la operación y el valor es la función que la implementa.

## ======== Analisis ======== ##
## Paso 1: Entender el problema: 
# Entrada: se usa una operación (+, -, *, /) y dos números, se ingresan numeros por el usuario en un bucle interactivo
# Proceso: en vez de usarse los if/elif, para decidir qué operación se ejecuta, se usa un diccionario 
#  donde cada clave es el símbolo de la operación y el valor es una función lambda que la ejecuta
# Salida: sale el resultado de la operación, es impreso en pantalla y se sigue repitiendo hasta que el usuario escriba "salir"

## Paso 2: Bosquejo
# operaciones = {
#  "+": suma,
#  "-": resta,
#  "*": multiplicación,
#  "/": división (o None si y == 0)
#}

#Simulación con op = "*", x = 4, y = 6:

#  1. Se busca "*" en el diccionario -> encuentra: lambda x, y: x * y
#  2. Se Ejecuta esa función con (4, 6) -> 4 * 6 = 24
#  3. Se Imprime "Resultado: 24"

#Si op = "/" y y = 0:
#  1. Se busca "/" -> encuentra: lambda x, y: x / y if y != 0 else None
#  2. Se ejecuta con (10, 0) -> como y == 0 -> retorna None
#  3. Se Imprime "Resultado: None"

#Si op = "%" (no existe en el diccionario):
#  1. "%" not in operaciones -> True
#  2. Imprimir "Operación no válida." y continuar el bucle

## Paso 3: Descubrir el patrón
# al usar la alternativa if/elif, se veria mal por que cada operación nueva significa un elif más, 
#  y el código se vuelve largo y repetitivo.
# En op se busca la función correcta, y (x, y) la ejecuta inmediatamente. Ademas agrega una operación nueva 
#  que significa agregar una línea al diccionario, sin tocar el resto de la lógica.
# al usar (op not in operaciones) se reemplaza limpiamente lo que sería un else final de validación.

## Paso 4: Escribir el código
def calculadora():
    operaciones = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y if y != 0 else None        
    }
    
    while True:
        op = input("Ingrese operación (+, -, *, /) o 'salir' para terminar: ")
        if op == "salir":
            break
        if op not in operaciones:
            print("Operación no válida.")
            continue
        
        try:
            x = float(input("Ingrese primer número: "))
            y = float(input("Ingrese segundo número: "))
        except ValueError:
            print("Entrada no válida. Intente de nuevo.")
            continue
        
        resultado = operaciones[op](x, y)
        print(f"Resultado: {resultado}")

calculadora()





