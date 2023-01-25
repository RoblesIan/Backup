"""
# bucle while
Estructura de controla que itera o repite la ejecucion de una 
serie de instrucciones hasta que se deje de cumplir la condicion.

while condition:
    bloque de instrucciones
    counting update
"""

print("\n---------- Ejemplo 1 ----------")
contador = 1

while contador <= 100:
    print(f"estoy en el numero {contador}")
    contador += 1


print("\n---------- Ejemplo 2 ----------")
contador = 1
muestrame = str(0)

while contador <= 100:
    muestrame = muestrame + ", " + str(contador)
    contador += 1

print(muestrame)

print("\n---------- Ejemplo 3 ----------")
numero = int(input("¿Que numero de la tabla deseas consultar?: "))
contador = 0

if not(numero >= 1 and numero <= 10):
    print("introduce un numero entero comprendido entre el 1 y el 10")
else:
    print("#### inicializando calculadora ####")
    while contador <= 10: 
        print(f"{numero} x {contador} = {numero*contador}")   
        contador += 1








