'''
Escribir un programa que pida al usuario un número entero y muestre por pantalla 
un triángulo rectángulo como el de más abajo, de altura el número introducido.

*
**
***
****
*****
'''

# Con while
# numero_de_pisos = int(input('Ingrese el numero de pisos: '))

# piso = 1
# while piso <= numero_de_pisos:
#     print(piso * '*')
#     piso += 1
    
# Con for

# numero_de_pisos = int(input('Ingrese el numero de pisos: '))

# v1
# for numero in range(1, numero_de_pisos + 1):
    # print(numero * '*')
    
# v2
# for numero in range(numero_de_pisos):
    # v1
    # print((numero+1) * '*')
    # v2
    # print(numero * '*' + '*')
    

'''
Escribir un programa que pida al usuario una palabra y luego muestre por
pantalla una a una las letras de la palabra introducida empezando por la última.
'''

# palabra = input('Ingrese una palabra: ')

# lista_caracteres = list(palabra)
# lista_invertida_caracteres = lista_caracteres[::-1]

# for caracter in lista_invertida_caracteres: # caracter = valor que me da la lista en cierta iteracion
#     print(caracter)


'''
Escribir un programa que muestre el print de todo lo que el usuario 
introduzca hasta que el usuario escriba “salir” que terminará.
'''

# v1
# texto_a_mostrar = ''
# while texto_a_mostrar.lower() != 'salir':
#     texto_a_mostrar = input('Ingrese un string: ')
#     print(texto_a_mostrar)

# v2
# while True:
#     texto_a_mostrar = input('Ingrese un string: ')
#     if texto_a_mostrar.lower() == 'salir':
#         break
#     print(texto_a_mostrar)


'''
Escribir un programa que pida al usuario un número entero y 
muestre por pantalla un triángulo rectángulo como el de más abajo.

1
3 1
5 3 1
7 5 3 1
9 7 5 3 1
'''