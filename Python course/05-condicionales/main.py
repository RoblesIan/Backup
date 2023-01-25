print("0\n ---------- Ejemplo 1 ----------")
color = input("¿Cual es mi color favorito?: ")

# if, si la condicion se cumple, ejecuta un bloque de comandos, else o si no, otro
if color == "rojo":
    print("Si !!")
else:
    print("No !!")


print("\n ---------- Ejemplo 2 ----------")
# ejemplo de uso de operadores de comparacion
year = int(input("¿En que año estamos?: "))

if year >= 2021:
    print("\nEstamos de 2021 en adelante !!")
else:
    print ("\nEs un año anterior a 2021")


print("\n ---------- Ejemplo 3 ----------")
nombre = "Ian"
ciudad = "Barcelona"
continente = "Europa"
edad = "19"
mayoria_edad = "18" 

if edad >= mayoria_edad:
    print(f"{nombre} es mayor de edad")
    if continente != "Europa":
        print("El usuario no es europeo")
    else:
        print(f"{nombre} es europeo y de {ciudad}")
else: 
    print(f"{nombre} NO es mayor de edad")


print("\n ---------- Ejemplo 4 ----------")
dia_semana = int(input("Que numero del dia de la semana es: "))

if dia_semana == 1:
    print("Hoy es lunes")
elif dia_semana == 2:
    print("Hoy es martes")
elif dia_semana == 3:
    print("Hoy es miercoles")
elif dia_semana == 4:
    print("Hoy es jueves")
elif dia_semana == 5:
    print("Hoy es viernes")
elif dia_semana == 6:
    print("Hoy es sabado")
elif dia_semana == 7:
    print("Hoy es domingo")


print("\n ---------- Ejemplo 5 ----------")
edad = int(input("¿Cuál es tu edad?: "))

if edad >= 18 and edad <= 65:
    print("Esta en edad de trabajar")
else:
    print("No está en edad de trabajar")


print("\n ---------- Ejemplo 6 ----------")

pais = input("¿En que pais vivís?: ")

if pais == "argentina" or pais == "mexico" or pais == "españa" or pais == "colombia":
    print("Tu pais es un pais de habla hispana !!")
else:
    print("Tu pais no es de habla hispana !!")


print("\n ---------- Ejemplo 7 ----------")

pais2 = input("¿En que pais vivís?: ")

if not (pais2 == "argentina" or pais2 == "mexico" or pais2 == "españa" or pais2 == "colombia"):
    print(f"{pais2} no es un pais de habla hispana !!")
else:
    print(f"{pais2} es un pais de habla hispana !!")


print("\n ---------- Ejemplo 8 ----------")

pais3 = input("¿En que pais vivís?: ")

if pais3 != "argentina" and pais3 != "mexico" and pais3 != "españa" and pais3 != "colombia":
    print(f"{pais3} no es un pais de habla hispana !!")
else:
    print(f"{pais3} es un pais de habla hispana !!")









