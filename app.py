# Este es un comentario de unas sola linea

'''
 Este es un comentario de 
 multiples lineas

'''

"""
    Estes es otro comentario
    de multiples lineas 
    con comillas sencillas
"""

from cgi import print_directory
from cmd import PROMPT
from operator import irshift
from posixpath import split


nombre = "shayd" # String 
cantidadMaterias = 3 # int
numeroDecimal = 15.8 # Float
esMayorEdad = True

diasSemana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"] # Lista = Array
listaDinamica = [0, "Hola", 12.5, [0,1]] # Lista dentro de una lista = Matriz

print(diasSemana[2]) # Miercoles 
print(listaDinamica[3][1]) # [0, 1] # 1

# Diccionarios - JSON - Objects

persona = {
    'nombre':  "Shayd",
    'apellido': "Ruano",
    'edad': 18,
    'materias': ["Base de datos II", "Lenguaje de cuarta generacion"],
}

print(persona["nombre"]) # Shayd
print(persona["materias"][1]) # Lenguaje de cuarta generacion 
print(persona) # Imprime todo

# Lista de diccionarios

personas=[
    {
    'nombre':  "Shayd",
    'apellido': "Ruano",
    'edad': 18,
    'materias': ["Base de datos II", "Lenguaje de cuarta generacion"],
    },
    {
    'nombre':  "Laura",
    'apellido': "Erazo",
    'edad': 16,
    'materias': ["Base de datos I", "Lenguaje orientado a objectos"],
    },
    {
    'nombre':  "Carla",
    'apellido': "Torres",
    'edad': 20,
    'materias': ["Lenguaje Orientado a Eventos"],
    }
]

print(personas[2]["materias"][0]) # Lenguaje Orientado a Eventos

#condiciones
esMayorEdad = True

if esMayorEdad:
    print("Es mayor de edad")
    print("Esto es del if")
else:
    print("No es mayor de edad")
    print('Esto es del else')

print('Mensaje de prueba')

for per in personas:
    print (per['nombre'])


