"""
# bucle for funciona tal que:

for variable in elemento_iterable (lista, rango, etc)
    bloque de instrucciones
"""

for i in range(0, 10): 
    print(i)

print("---------- Ejemplo 1 ----------")

numero = int(input("Que numero de la tabla quieres consultar?: "))

if numero <1:
    numero = 1

print(f"\nMostrando la tabla del {numero}")

for i in range (0,11):
    print(f"{numero} x {i} = {i*numero}")
else: 
    print("table finalizada")








