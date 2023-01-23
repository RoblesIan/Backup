# Una variable es un contenedor de información

# Asignamos valores
string = "Informacion tipo texto"
number = 2
float = 3.6
nada = None

# Cambiamos valores
cambio = "Info a ser cambiada"
cambio = 1

# Mostramos valores
print(string)
print(number)
print(float)
print(cambio)

# Concatenación
nombre = "Ian"
apellido = "Robles"
nombreCompleto = nombre + " " + apellido

print(nombreCompleto)
print(nombre + " " + apellido)
print(f"{nombre} {apellido}")
print("{} {}".format(nombre, apellido))

# esto no es concatenar, aca solo le damos las variables por parámetro y print las muestra en orden siempre y con un espacio por default
print(nombre, apellido)

