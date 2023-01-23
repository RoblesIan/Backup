# Introduciendo comillas dentro de un string de modo que no genere conflicto con las comillas existentes y sin afectar su funcionalidad
mi_texto = "Soy \"Ian Robles\" entre comillas"
mi_texto2 = "Soy 'Ian Robles2' entre comillas"
mi_texto3 = 'Soy "Ian Robles3" entre comillas'

# valores especiales

# salto de linea
mi_texto_unido1 = mi_texto + "\n" + mi_texto2
print(mi_texto_unido1)

# tabulacion
mi_texto_unido1 = mi_texto + "\t" + mi_texto2
print(mi_texto_unido1)

# borra todo lo que haya detras de el
mi_texto_unido1 = mi_texto + "\r" + mi_texto2
print(mi_texto_unido1)


