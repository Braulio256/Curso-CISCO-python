#Asi como en las operaciones aritmeticas hay operadores tambien existen operadores de comparacion
#Entre ellos estan:
#== Operador igual a
#!= Operador diferente de
#< Operador menor que
#> Operador mayor que
#<= Operador menor o igual que
#>= Operador mayor o igual que
#Estos operadores entregaran un valor booleano como respuesta
comp1 = 45<=30
comp2 = 45>=30
comp3 = 45==30
comp4 = 45!=30
print(comp1)
print(comp2)
print(comp3)
print(comp4)

#Estos operadores se suelen utilizar en funciones condicionales como if y elif
a = float(input("Ingrese un numero: "))
if a>0:
    print("El numero es positivo")
elif a<0:
    print("El numero es negativo")
else:
    print("El numero es cero")

a = input("Ingrese un nombre: ")
b = input("Ingrese otro nombre: ")
if a == b:
    print("Los nombres son iguales")
else:
    print("Los nombres son diferentes")

#Otra forma de comparar valores nos lleva a la introduccion de los bucles
# Se leen tres números.
number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))
number3 = int(input("Ingresa el tercer número: "))

# Verifica cuál de los números es el mayor
# y pásalo a la variable largest_number.

largest_number = max(number1, number2, number3)

# Imprime el resultado.
print("El número más grande es:", largest_number)