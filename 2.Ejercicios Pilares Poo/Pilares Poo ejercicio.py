## Clase Temperatura que almacene internamente en Celsius. 
# Expone las propiedades celsius, fahrenheit y kelvin, todas con getter y setter — asignar cualquiera de las tres debe recalcular las demás.

## ======== Analisis ======== ##
## Paso 1: Entender el problema:
# Entrada: Se crea operaciones sobre la temperatura  celsius, fahrenheit o kelvin
# Proceso: se empieza a encapsular celsius, exponer las 3 escalas con property y recalcular al vuelo
# Salida: se ve el estado de la temperatura en las 3 escalas
 
## Paso 2: Bosquejo
# temp = Temperatura(30)
#                         → _celsius = 30
# print(temp)             → "30.00 °C, 86.00 °F, 303.15 K"

# temp.fahrenheit = 150
#                         → _celsius = (150-32) * 5/9 = 65.56
# print(temp)             → "65.56 °C, 150.00 °F, 338.71 K"

# temp.celsius = 100
#                         → _celsius = 100 

# temp.kelvin = 0
#                         → _celsius = 0 - 273.15 = -273.15

## Paso 3: Descubrir el patrón

# Solo existe un atributo real: _celsius ya que las propiedades fahrenheit y kelvin no guardan su propio valor ademas,
# cada una tiene un getter que calcula su valor a partir de _celsius, y un setter que convierte el valor recibido y lo guarda en _celsius.

# Mas importante, sin importar cuál de las tres propiedades se les asigne, siempre se termina actualizando a la misma fuente de verdad. 
# Y como los getters recalculan cada vez que se leen, las tres escalas siempre están sincronizadas y
# nunca puede haber un valor de Fahrenheit que no corresponda al Celsius actual.

# Al tener setter en las tres que son celsius, fahrenheit, kelvin, la clase permite escribir por cualquier puerta lado
# pero siempre llevan al mismo lugar (_celsius).


## Paso 4: Escribir el código
class Temperatura:
    def __init__(self, celsius=0):
        self._celsius = celsius
        
    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, valor):
        self._celsius = valor
    
    @property
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32
    
    @fahrenheit.setter
    def fahrenheit(self, valor):
        self._celsius = (valor - 32) * 5/9
        
    @property
    def kelvin(self):
        return self._celsius + 273.15
    
    @kelvin.setter
    def kelvin(self, valor):
        self._celsius = valor - 273.15
    
    def __str__(self):
        return f"{self._celsius:.2f} °C, {self.fahrenheit:.2f} °F, {self.kelvin:.2f} K"


temp = Temperatura(30)
print(temp)     
temp.fahrenheit = 150
print(temp)

## -------------------------------------------------------------------------------------------- ##

## Clase base Descuento con método aplicar(precio). 
# Hijas: SinDescuento, PorcentualDescuento(porcentaje), MontoFijoDescuento(monto). 
# Función calcular_total(precio, descuento) que aplique el descuento y retorne el precio final.

## ======== Analisis ======== ##
## Paso 1: Entender el problema:
# Entrada: Se crea el Precio y el tipo de descuento
# Proceso: se aplica polimórficamente la lógica de descuento correspondiente
# Salida: se declara el Precio final después del descuento
## Paso 2: Bosquejo

# calcular_total(170, SinDescuento())            → aplicar(170) = 170
# calcular_total(170, PorcentualDescuento(17))   → aplicar(170) = 170 - (170*17/100) = 141.1
# calcular_total(170, MontoFijoDescuento(15))    → aplicar(170) = max(0, 170-15) = 155

## Paso 3: Descubrir el patrón

# El poder de este diseño está en calcular_total(precio, descuento): esta función no necesita saber qué tipo de descuento recibe. 
# Solo llama a descuento.aplicar(precio), y es cada subclase la que decide cómo calcular el resultado. ya que esto es polimorfismo puro.

# La clase base Descuento no calcula nada por sí sola, porque su método aplicar solo existe para lanzar NotImplementedError, 
# obligando a que toda subclase lo sobrescriba. Es un contrato: "si eres un descuento, debes saber aplicarte a un precio".

# En MontoFijoDescuento, se usa el max porque evita que el precio final sea negativo si el monto fijo es mayor al precio original — una validación
# importante que PorcentualDescuento no necesita, porque un porcentaje entre 0 y 100 nunca produce resultados negativos.


## Paso 4: Escribir el código
class Descuento:
    def aplicar(self, precio):
        raise NotImplementedError
    
class sinDescuento(Descuento):
    def aplicar(self, precio):
        return precio

class PorcentualDescuento(Descuento):
    def __init__(self, porcentaje):
        self.porcentaje = porcentaje
    
    def aplicar(self, precio):
        return precio - (precio * self.porcentaje / 100)
    
class MontoFijoDescuento(Descuento):
    def __init__(self, monto):
        self.monto = monto
        
    def aplicar(self, precio):
        return max (0, precio - self.monto )
    
def calcular_total(precio, descuento):
    return descuento.aplicar(precio)


print(calcular_total(170, sinDescuento()))           
print(calcular_total(170, PorcentualDescuento(17)))  
print(calcular_total(170, MontoFijoDescuento(15)))  


## Clase Estudiante con nombre, cédula y una lista privada de notas (__notas). 
# Método agregar_nota(n) que solo acepte valores entre 0 y 10. Propiedad calculada promedio.
# Propiedad calculada aprobado (True si promedio >= 7).

## ======== Analisis ======== ##
## Paso 1: Entender el problema:
# Entrada: Se crea operaciones sobre el estudiante el cual es agregar notas
# Proceso: se encapsula las notas,se expone con property, se calcula el promedio y estado dinámicamente
# Salida: termina en el estado del estudiante y su condición (aprobado/reprobado)
 
## Paso 2: Bosquejo
# est = Estudiante("Joel", "0953553245")
# est.agregar_nota(10)     → __notas = [10]
# est.agregar_nota(7)      → __notas = [10, 7]
# est.agregar_nota(9)      → __notas = [10, 7, 9]
# est.notas                → [10, 7, 9]  (copia protegida)
# est.promedio             → 8.666666... (26/3)
# est.aprobado             → True (8.67 >= 7)
# est.__notas = [999]       → ERROR: no existe tal atributo directamente
#                           (el name mangling lo convierte en _Estudiante__notas)
# print(est)                → "Joel: prom=8.67 — Aprobado"

## Paso 3: Descubrir el patrón
# En  __notas se activa el name mangling: En Python se renombra internamente a _Estudiante__notas, lo que dificulta 
# el acceso accidental desde fuera de la clase ya que es un encapsulamiento más fuerte que un simple guion bajo.

# En notas como property se retorna list(self.__notas), que es una copia, no la lista original. 
# ya que esto evita que alguien modifique el estado interno sin pasar por la validación de agregar_nota.

# El promedio es calculado, no almacenado: se recalcula cada vez que se accede, así que siempre refleja el estado actual de __notas.
# No hay riesgo de que quede "desactualizado".

# En aprobado depende de promedio, formando una cadena de propiedades calculadas: cambiar las notas propaga automáticamente el cambio a promedio y a aprobado, sin que el programador tenga que actualizar nada manualmente.
# El redondeo se hace solo en la presentación (:.2f en __str__), no en el cálculo interno — así se preserva la precisión completa para cualquier uso posterior de promedio.


## Paso 4: Escribir el código
class Estudiante:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula
        self.__notas = []
        
    def agregar_nota(self, n):
        if not 0 <= n <= 10:           
            raise ValueError ("Nota entre 0 y 10")
        self.__notas.append(n)
    
    @property
    def notas(self):
        return list(self.__notas)
    
    @property
    def promedio(self):
        if not self.__notas:
            return 0
        return sum(self.__notas) / len(self.__notas)

    @property
    def aprobado(self):
        return self.promedio >= 7

    def __str__(self):
        estado = "Aprobado" if self.aprobado else "Reprobado"
        return f"{self.nombre}: prom={self.promedio:.2f} — {estado}"


est = Estudiante("Joel", "0953553245")
for n in [10, 7, 9]:
    est.agregar_nota(n)
print(est)
    