#+ operador de suma
#- operador de resta
#* operador de multiplicación
#/ operador de división
#// operador de división entera
#% operador de residuo
#** operador de exponenciación

#Ejemplos de los operadores
print(5+5)
print(15-5)
print(5*5)
print(40/7)
print(45//7)
print(45%7)
print(2**3)

#Los operadores tienen prioridad
#** operador de exponenciación
#+, - (como operadores unarios estos tienen mas prioridad cuando estan acompañados del operador de exponenciación)
#*, /, //, %
#+, - (y por ultimo los operadores de suma y resta)

#Ejemplo
print(2**3+5)
print(3**4-4)
print(3*4/5)
print(5+8/2)

#Tambien se pueden usar parentesis para separar operaciones
print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)