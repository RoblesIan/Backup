"""
Funciones: 
Una funcion es un conjunto de instrucciones agrupadas bajo
un nombre concreto que pueden reutilizarse haciendo un 
llamado a la misma, tantas veces como quiseramos. La funcion
puede recibir parámetros para ser utilizados dentro de su 
función. 
"""

# Ejemplo 1
print("\n---------- Ejemplo 1 ----------")

# vamos a realizar una implementacion de funcion sin parámetros

# definimos el nombre de la funcion y que bloque de comandos va a ejecutar
def muestraNombre():
    print("Roberto \nCristina \nRigoberto \nAlberto \ntodo lo que termine en berto")

# hacemos el llamado a la funcion
muestraNombre()


# Ejemplo 2
print("\n---------- Ejemplo 2 ----------")

# definimos funcion y que parametro utilizaremos
def mostrarTuNombre(nombre):
    print(f"Tu nombre es: {nombre}")

# definimos el parametro con un input
nombre = input("¿Cuál es tu nombre?: ")
# llamamos a la funcion
mostrarTuNombre(nombre)

"""
Podriamos cambiar el valor del parametro tal que:

nombre = input("¿Cuál es tu nombre?: ")
def mostrarTuNombre(nombre):
    print(f"Tu nombre es: {nombre}")

mostrarTuNombre("ian")
mostrarTuNombre("lautaro")
mostrarTuNombre("nazareno")
mostrarTuNombre("robles")
"""

# Ejemplo 3
print("\n---------- Ejemplo 3 ----------")
def Tablas(numero):
    for i in range (0,11):
        print(f"{numero} x {i} = {numero*i}")

Tablas(int(input("¿La tabla de que número deseas consultar?: ")))


# Ejemplo 4
print("\n---------- Ejemplo 4 ----------")
# Parámetros opcionales

"""
Dandole un valor por default hacemos que si el usuario no declarara un parámetro, el valor quede 
distinto de null, de modo que no nos arroje error.
"""

def getEmpleado(nombre, id = None):
    print(f"empleado\nNombre: {nombre}\n")
    if id != None:
        print(f"ID: {id}")

getEmpleado("Ian")
# y si queremos pasarle el parametro: getEmpleado("Ian", 45748529)


# Ejemplo 5
print("\n---------- Ejemplo 5 ----------")
# Parámetros opcionales, return, devolucion de datos

def saludame(nombre):
    saludo = f"Hola, saludos {nombre}"
    return saludo

"""
con la funcion return, la funcion guarda en si misma el valor del parametro que le estamos pasando a 
return, pero solo la guarda en si misma, para poder verla por pantalla, como con cualquier valor, 
tendremos que aplicarle un return
"""
print(saludame("ian"))


# Ejemplo 5
print("\n---------- Ejemplo 5 ----------")
# Funciones dentro de funciones

def getNombre(nombre):
    texto = f"El nombre es: {nombre}"
    return texto

def getApellidos(apellidos):
    texto = f"Los apellidos son: {apellidos}"
    return texto

def nombreApellido (nombre, apellidos):
    texto = getNombre(nombre) + "\n" + getApellidos(apellidos)


print(nombreApellido("Ian", "Robles"))


# Ejemplo 5
print("\n---------- Ejemplo 5 ----------")
# Funciones lambda, son funciones anonimas sin nombre, que ocupan solo 1 linea para funcionalidades pequeñas

# la sentencio con el nombre, el parametro a utilizar, y con 2 puntos que quiero que haga o devuelva
dime_el_año = lambda year: f"el año es {year}"

