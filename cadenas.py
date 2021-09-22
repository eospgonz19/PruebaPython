texto = "Bievenido al horrible mundo del puto amo 1234"
texto2 = "Toloza es un completo imbecil"

print(texto)
print(texto.lower())
print(texto.upper())
print(texto.title())

print(texto2)
print(texto2.lower())
print(texto2.upper())
print(texto2.title()) #convierte una cadena a un formato de titulo
print(texto.find("al"))  #Posición donde encuentra la cadena o porción

print(texto.count("e")) #Cantidad de ocurrencias de una letra o porción

textoFinal = texto.replace("e", "3") #Reemplaza la establecia por lo que indiques
print(textoFinal)

valor = texto.isnumeric() #Arroja true o false dependiendo si es un número.
print(valor)

cadenaSeparada = texto.split(" ")
print(cadenaSeparada)