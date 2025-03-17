#Entre los operadores lógicos tenemos
#El operador and
#El operador or
#El operador not

var1 = True
var2 = False
print(var1 and var2)
print()
print(var1 or var2)
print()
print(not var1)
print()
print(not var2)

#Entre los operadores bit a bit tenemos
#Operador & (conjunción)
#Operador | (disyunción)
#Operador ~ (negación)
#Operador ^ (or exclusivo[xor])

print("\n\n")
i = 1
j = 0
print(i & j)
print()
print(i | j)
print()
print(~i)
print()
print(i ^ j)

#Desplazamiento binario a la izquierda y derecha
#Operador de cambio derecha >>
#Operador de cambio izquierda <<
print("\n\n")
var = 17
var_right = var >> 1
var_left = var << 2
print(var, var_left, var_right)

#Ejemplo de los operadores bit a bit
print("\n\n")
x = 4
y = 1

a = x & y
b = x | y
c = ~x
d = x ^ 5
e = x >> 2
f = x << 2

print(a, b, c, d, e, f)