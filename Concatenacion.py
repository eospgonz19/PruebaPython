texto1 = "Hola"
texto2 = "Mundo"
textofinal = texto1 + " " + texto2
print(textofinal)

saludoFinal = "Saludo: {1} {0}".format(texto1, texto2) #organiza le texto según el orden que desees que imprima dependiendo de la posición
print(saludoFinal)

saludoFinal2 = "Saludo: {x} {x}".format(x=texto1, y=texto2)#organiza le texto según el orden que desees que imprima dependiendo de la variable asignada
print(saludoFinal2)