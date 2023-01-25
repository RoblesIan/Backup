nombre = "ian"

# funciones generales

# imprimir por pantalla
print(nombre)

# nos da el tipo de una variable
print(type(nombre))

# detectar el tipo que le pasemos por parametro
if isinstance(nombre, str): # arroja como valor True si el primer parametro contiene el valor del tipo 
                            # que le pasemos al segundo parametro, caso contrario false
    print("Esta variable es un string")
else: 
    print("Esta variable NO es un string")

# suprime los espacios detras del primer caracter, y delante del ultimo,

frase = "          hola contenido "
print(frase) # vemos la frase original
print(frase.strip())

# eliminar variables
year = 2022
print(year) # mostramos variable
del year    # eliminamos el valor
# print(year) # nos arroja error porque el valor es nulo

# longitud de caracteres de una variable
texto = "AOSIDn  aopsmdo "
print(len(texto)) # nos arroja en valor numerico la cantidad de caracteres que tiene la variable que 
                  # le pasamos por parámetro

# buscar caracteres 
frase = "Hola soy una frase soy"
print(frase.find("soy")) # find nos arroja como valor el numero de la posicion del primer caracter de la palabra que le pasamos por parametro que primero encuentre

# reemplazar palabras en un string
reemplazo = frase.replace("soy", "moto") # reemplaza en el string que le indiquemos, la palabra 
                                         # especifica que le pasemos como primer parametro, por la 
                                         # que le pasemos por el segundo parametro, todas las veces 
                                         # que esa palabra se repita
print(reemplazo)

# mayúsculas y minúsculas
print(nombre) # nombre sin cambios
print(nombre.lower()) # nombre completamente en minúsculas
print(nombre.upper() # nombre completamente en mayúsculas





