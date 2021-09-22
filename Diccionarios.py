""""
Diccionarios: son estructuras de datos que nos permiten almacenar distintos valores

Es que los daos se almacenan asociados a una clave única, tenemos una relación clave:valor

los elementos almacenados están en desorden, el orden es indiferente a la forma de almacenamiento


"""

miDiccionario = {"Colombia":"Medellín","Alemania":"Berlin","Portugal":"Lisboa"}
print(miDiccionario["Portugal"])
print(miDiccionario)

miDiccionario["Venezuela"] = "Caracas"
print(miDiccionario)

miDiccionario["Colombia"] = "Bogotá"
print(miDiccionario)

del miDiccionario["Venezuela"]
print(miDiccionario)

dic2 = {"Garcia": "Oscar", 25:True, "Sueldo": 150.80}
print(dic2["Garcia"])

llaves=("España", "Francia", "England")
dicPaises={llaves[0]:"Madrid", llaves[1]:"Paris", llaves[2]:"London"}
print(dicPaises)


datosPersonales={"Apellido":"Garcia", "Años":{1: 2010, 2: 2011, 3: 2012, 4: 2013, 5: 2014}}
print(datosPersonales)
print(datosPersonales["Años"])

print(datosPersonales.get('Apellido', "Oscar"))

print(datosPersonales.keys())
valores=list(datosPersonales.values())
print(valores)

valores1 = tuple(datosPersonales.values())
print(valores1)