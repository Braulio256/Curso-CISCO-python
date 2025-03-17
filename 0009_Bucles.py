#Bucle while
#Ejemplos
# Almacena el actual número más grande aquí.
largest_number = -999999999

# Ingresa el primer valor.
number = int(input("Introduce un número o escribe 0 para detener: "))

# Si el número no es igual a -1, continuaremos
while number != 0:
    # ¿Es el número más grande que el valor de largest_number?
    if number > largest_number:
        # Sí si, se actualiza largest_number.
        largest_number = number
    # Ingresa el siguiente número.
    number = int(input("Introduce un número o escribe 0 para detener: "))

# Imprime el número más grande.
print("El número más grande es:", largest_number,"\n")
#----------------------------------------------------------------------------------------------
#Este de aqui es un contador decreciente
counter = 5
while counter:
    print("Dentro del bucle.", counter)
    counter -= 1
print("Fuera del bucle.", counter)

#Bucle for
#Equivalente en bucle while
print("\n\n")
i = 0
while i < 5:
    print(i)
    i += 1
#Ejemplos
print("\n\n")
for i in range(5):
    print(i)
    i += 1
    pass

print("\n\n")
res = 1
for exponente in range(16):
    print("2 a la potencia de", exponente, "es", res)
    res *= 2

