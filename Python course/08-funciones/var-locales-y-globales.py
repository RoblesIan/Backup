"""
Variables locales: se definen dentro de una funcion y no
se puede usar fuera de ella, al menos que le hagamos un 
return de modo que expresemos su valor.

Variables globales: Son las que se declaran fuera de una funcion
y estan disponibles dentro y fuera de ellas.
"""

var_global = 907
print(var_global)

def holaMundo():
    print(var_global) # la var global puede ser utilizada en todo momento y lugar, globalmente

    var_local = 908
    print(var_local) # la var local es accesible dentro de la funcion

    global var_definida_global # convierto una var local a una global
    var_definida_global = 909
    print(var_definida_global) # accedo a la var convertida localmente

# print(var_local) # pero la var local no es accesible por fuera de la funcion, al menos que declare una var globalmente con el mismo nombre
print(var_definida_global) # y tambien accedo a la variable convertida fuera de la funcion






