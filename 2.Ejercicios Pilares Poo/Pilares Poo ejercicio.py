## Clase Temperatura que almacene internamente en Celsius. 
# Expone las propiedades celsius, fahrenheit y kelvin, todas con getter y setter — asignar cualquiera de las tres debe recalcular las demás.

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


e = Estudiante("Ana", "0912")
for n in [8, 6, 9]:
    e.agregar_nota(n)
print(e)
    

    
    
    
    
    
    
    