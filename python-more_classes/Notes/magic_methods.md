# Magic Methods

![e1064baf-759f-4741-8aab-4a2173e87855_2128x2826](https://github.com/user-attachments/assets/c7367933-f2b3-4a36-a747-a94709a9e881)

## En Python, los nombres que comienzan y terminan con dos guiones bajos (__) se conocen como **“dunder”** **(double underscore)** o **“magic methods”**. Estos métodos tienen un propósito especial y son utilizados por el intérprete de Python para realizar ciertas operaciones. Aquí tienes algunos ejemplos y sus usos:

### Ejemplos de métodos mágicos:
--------------------------------------------------------------------------
### **__init__:**
Es el constructor de una clase. Se llama automáticamente cuando se crea una nueva instancia de la clase.

=====================================
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

p = Persona("Ada", 30)
=====================================
----------------------------------------------------------------------------
### **__str__:** 
El método mágico __str__ en Python se utiliza para definir una representación en forma de cadena de un objeto. Este método es llamado cuando se usa la función print() o str() en un objeto. Su propósito principal es proporcionar una salida legible y amigable para los humanos.

Propósito de __str__
Legibilidad: Proporciona una representación en cadena que es fácil de leer y entender.
Interfaz de Usuario: Se utiliza principalmente para mostrar información al usuario final de manera clara y concisa.

=====================================
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"{self.nombre}, {self.edad} años"

p = Persona("Ada", 30)

print(p)  # Salida: Ada, 30 años
=====================================
---------------------------------------------------------------------------
### **__repr__:**
Este método mágico en Python se utiliza para definir la representación oficial de un objeto. Su propósito principal es proporcionar una cadena que, idealmente, podría ser utilizada para recrear el objeto con la función eval().

Propósito de __repr__
Depuración: Proporciona una representación detallada y precisa del objeto, útil para los desarrolladores.
Recreación del Objeto: La cadena devuelta por __repr__ debería ser una expresión válida de Python que, cuando se pasa a eval(), recrea el objeto original.
=====================================
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __repr__(self):
        return f"Persona('{self.nombre}', {self.edad})"

p = Persona("Ada", 30)

print(repr(p))  # Salida: Persona('Ada', 30)
=====================================
---------------------------------------------------------------------------

### **__len__:**
 El método mágico __len__ en Python se utiliza para definir la longitud de un objeto. Este método es invocado automáticamente cuando se utiliza la función len() en una instancia de la clase que lo implementa. Es especialmente útil para estructuras de datos personalizadas, permitiendo que se comporten de manera similar a las listas, cadenas y otros contenedores integrados en Python.

Propósito de __len__
Obtener la longitud: Permite definir cómo se calcula la longitud de un objeto.
Compatibilidad con len(): Hace que los objetos personalizados sean compatibles con la función len().

=====================================
class Grupo:
    def __init__(self, miembros):
        self.miembros = miembros

    def __len__(self):
        return len(self.miembros)

g = Grupo(["Ada", "Grace", "Alan"])
print(len(g))  # Salida: 3
=====================================
-----------------------------------------------------------------------------

### **__getitem__:**
El método mágico __getitem__ en Python permite a las instancias de una clase utilizar el operador de corchetes [] para acceder a sus elementos. Este método se invoca cuando se usa la notación objeto[indice], y define cómo se debe comportar el objeto al acceder a sus elementos mediante índices o claves.

Propósito de __getitem__
Acceso a Elementos: Permite definir cómo se acceden los elementos de un objeto.
Compatibilidad con Índices y Claves: Hace que los objetos personalizados sean compatibles con la notación de corchetes para acceder a sus elementos.

=====================================
class MiLista:
    def __init__(self, elementos):
        self.elementos = elementos

    def __getitem__(self, indice):
        return self.elementos[indice]

ml = MiLista([1, 2, 3])
print(ml[1])  # Salida: 2
=====================================
---------------------------------------------------------------------------

## Importancia y uso
Estos métodos mágicos permiten personalizar el comportamiento de las operaciones básicas en los objetos de tus clases. Son especialmente útiles para hacer que tus clases se comporten de manera más intuitiva y para integrarse mejor con las funciones y operadores de Python.

>>> This is an Holberton School Project Author: Alexis Rodriguez Rodriguez Location: Montevideo. Uruguay September 2024

@ 2024 Alexis-Holberton School --All right reserved--
