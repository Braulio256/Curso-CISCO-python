anything = input("Dime lo que sea...")#La funcion input() permite al usuario interactuar dando valores a las variables
print("Hmm...", anything, "...¿en serio?")

#Para que lo que ingrese el usuario se pueda utilizar en una operacion matematica se debe convertir el tipo de variable
anything = float(input("Ingresa un número: "))
something = anything ** 2.0
print(anything, "a la potencia de 2 es", something)

#En los operadores cadena tenemos el + y el *
print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")

#Ejemplo de lo que se puede hacer con lo visto anteriormente
leg_a = float(input("Ingresa la longitud del primer cateto: "))
leg_b = float(input("Ingresa la longitud del segundo cateto: "))
print("La longitud de la hipotenusa es " + str((leg_a**2 + leg_b**2) ** .5))