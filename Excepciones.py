#Excepción: Error en tiempo de ejecución (durante la ejecución de un programa)

print("Hola, soy Estiven, tu Calculador virtual")

numero1 = int(input("Ingresa número a dividir: "))
numero2 = int(input("Ingresa número divisor: "))

#print("La divición de {0} entre {1} es: {2}".format(numero1, numero2, (numero1 / numero2)))

try:
    resultado = numero1 / numero2
    print("El resultadode la división entre {0} y {1} es: {2}".format(numero1, numero2, (numero1 / numero2)))
except ZeroDivisionError:
    print("No se puede dividir entre 0...")

finally:
    print("Yo siempre aparezco.")

print("Aquí termina mi programa.")