# open, close (w, r, a)

# https://docs.python.org/3/library/functions.html#open

# archivo_abierto = open('texto.txt', 'w')
# print(type(archivo_abierto))

# # Trabajamos con el archivo
# #  y al finalizar lo debemos cerrar

# archivo_abierto.close()




# archivo_abierto = open('prueba.txt', 'w')
# archivo_abierto.write('Escribiendo mi primer linea')
# archivo_abierto.close()
# archivo_abierto.write('eaea ea ea')
# print(archivo_abierto)


# archivo_abierto = open('prueba.txt', 'a')
# archivo_abierto.write('\nEscribiendo mi primer linea')
# archivo_abierto.close()



# archivo_abierto = open('carpeta/prueba.txt', 'w')
# archivo_abierto.write('Escribiendo mi primer linea')
# archivo_abierto.close()

# archivo_abierto = open('../prueba.txt', 'w')
# archivo_abierto.write('Escribiendo mi primer linea')
# archivo_abierto.close()


# archivo = open('miHobbieFavorito.txt', 'w')
# for numero in range(1, 4):
#     archivo.write(input(f'Ingrese su hobbie numero {numero}: ') + '\n')
# archivo.close()



# with open('texto.txt', 'w') as archivo_abierto:
#     # Trabajamos con el archivo
# # Una vez fuera del with el archivo se cierra solo

# with open('miHobbieFavorito.txt', 'w') as archivo:
#     for numero in range(1, 4):
#         archivo.write(input(f'Ingrese su hobbie numero {numero}: ') + '\n')
# print('Aca ya estamos por fuera del with')



# write

# archivo_abierto = open('archivos_clase8/texto.txt', 'w')
# archivo_abierto = open('archivos_clase8/texto123.txt', 'a')
# archivo_abierto = open('archivos_clase8/texto123.txt', 'w')

# archivo_abierto.write('Esto es una prueba\n')
# archivo_abierto.write('Soy otra cosa')
# archivo_abierto.write('Pise el texto')

# archivo_abierto.close()


# archivo_abierto = open('archivos_clase8/texto123.txt', 'w')

# archivo_abierto.write('Pepe')

# archivo_abierto.close()

# read, readline, readlines


# archivo = open('miHobbieFavorito.txt', 'r')
# # print(archivo.read())
# texto_del_archivo = archivo.read()
# print(texto_del_archivo)
# print(archivo)
# archivo.close()
# # print(archivo.read())
# print(texto_del_archivo)


# archivo = open('miHobbieFavorito.txt', 'r')
# print(archivo.read())
# print('=============================')
# print(archivo.read())
# archivo.close()


# archivo = open('miHobbieFavorito.txt', 'r')
# linea1_del_archivo = archivo.readline()
# print(linea1_del_archivo)
# linea2_del_archivo = archivo.readline()
# print(linea2_del_archivo)
# linea3_del_archivo = archivo.readline()
# print(linea3_del_archivo)
# archivo.close()


# archivo = open('miHobbieFavorito.txt', 'r')
# print(archivo.readline())
# print('=============================')
# print(archivo.readline())
# print('=============================')
# print(archivo.readline())
# print('=============================')
# print(archivo.readline())
# print(archivo.readline())
# print(archivo.readline())
# print(archivo.readline())
# print(archivo.readline())
# print(archivo.readline())
# print(archivo.readline())
# print(archivo.readline())
# archivo.close()


# archivo = open('miHobbieFavorito.txt', 'r')
# listado_de_lineas_del_archivo = archivo.readlines()
# print(listado_de_lineas_del_archivo)
# archivo.close()


# archivo = open('miHobbieFavorito.txt', 'r')
# print(archivo.readlines())
# print('=============================')
# print(archivo.readlines())
# archivo.close()


# archivo = open('miHobbieFavorito.txt', 'r')
# print(archivo.read())
# print('=============================')
# print(archivo.read())
# print('=============================')
# # archivo.seek(0)
# archivo.seek(8)
# # print(archivo.read())
# print(archivo.readline())
# print(archivo.readlines())
# print('=============================')
# archivo.seek(0)
# print(archivo.readlines())
# archivo.close()




# JSON -> js object notation 
# lista = [1,2,3,4,5,6]

# mi_dic = {
#     'clave1': 1, 
#     'clave2': 2, 
#     'clave3': 3,
#     'clave4': 4,
#     'clave5': 5,
#     'clave6': 6,
#     'clave7': 7,
#     'clave8': 8,
#     'clave9': 9,
#     'lista': lista,
# }


# import json

# with open('test.json', 'w') as f:
#     json.dump(mi_dic, f, indent=2)
    # json.dump(lista, f, indent=2)


# with open('test.json', 'r') as f:
#     datos = json.load(f)
#     print(datos)
#     print(type(datos))







# archivo_abierto = open(r'datos.txt', 'r', encoding="utf-8")
# archivo_abierto = open(r'..\datos.txt', 'r')
# archivo_abierto = open(r'C:\Source Code\Coder\41765\datos.txt', 'r')
# print(type(archivo_abierto))

# print(archivo_abierto.read())
# print('----------------')
# print(archivo_abierto.read())
# print('----------------')

# print(archivo_abierto.readline())
# print(archivo_abierto.readline())
# print(archivo_abierto.readline())

# print(archivo_abierto.readlines())
# print(archivo_abierto.readlines())
# print(len(archivo_abierto.readlines()))

# archivo_abierto.close()

# archivo_abierto = open(r'datos.txt', 'r', encoding="utf-8")

# texto = archivo_abierto.read()

# print(archivo_abierto.read())
# archivo_abierto.close()

# print('----------------')
# print('----------------')
# print(texto)
# print('----------------')
# print('----------------')
# print(texto)


# seek

# archivo_abierto = open(r'datos.txt', 'r', encoding="utf-8")
# archivo_abierto = open(r'datos.txt', 'w', encoding="utf-8")
# archivo_abierto = open(r'datos.txt', 'a', encoding="utf-8")

# print(archivo_abierto.read())
# archivo_abierto.seek(1)
# print('----------------')
# print(archivo_abierto.read())

# print(archivo_abierto.readline())
# archivo_abierto.seek(2)
# print('----------------')
# print(archivo_abierto.readline())

# lineas = archivo_abierto.readlines()
# print(archivo_abierto.readlines())

# archivo_abierto.seek(25)

# print(archivo_abierto.readlines())


# archivo_abierto.close()

# nuevas_lineas = []
# for linea in lineas:
#     nuevas_lineas.append(linea.upper())
    
# print(nuevas_lineas)

# archivo_abierto = open(r'datos.txt', 'w', encoding="utf-8")
# archivo.write(''.join(nuevas_lineas))
# archivo_abierto.write(nuevas_lineas[2])
# archivo_abierto.close()

# auto = {
#     'motor': 'v8', 
#     'color': 'Negro',
#     'vidrios': (6, 'blindadas'),
#     'pasajeros': 4,
# }

# with open('archivos_clase8/datos_auto.txt', 'w') as archivo:
#     archivo.write(f'{auto["motor"]}\n')
#     archivo.write(f'{auto["color"]}\n')
#     archivo.write(f'{auto["vidrios"]}\n')
#     archivo.write(f'{auto["pasajeros"]}\n')
#     archivo.write(f'{auto.get("Ricardo", "otro valor")}\n')

# with open('archivos_clase8/datos_auto.txt', 'w') as archivo:
#     archivo.write('''
# auto = {
#     'motor': 'v8', 
#     'color': 'Negro',
#     'vidrios': (6, 'blindadas'),
#     'pasajeros': 4,
# }
# ''')
    
# json

# auto = {
#     'motor': 'v8', 
#     'color': 'Negro',
#     'vidrios': (6, 'blindadas'),
#     'pasajeros': 4,
# }

# lista = [1,2,3,4,5,6,7]

# import json

# # dump
# with open('archivos_clase8/mi_archivo.json', 'w') as archivo_para_guardar:
#     json.dump(auto, archivo_para_guardar, indent=4)
#     # json.dump(lista, archivo_para_guardar, indent=4)

# # load
# with open('archivos_clase8/mi_archivo.json', 'r') as archivo_para_leer:
#     datos = json.load(archivo_para_leer)
#     print(datos)
#     print(type(datos))


# import pandas as pd

# datos = pd.read_csv(r'dataset_viajes_sube.csv')
# print(datos)
# # NOT A NUMBER (NaN) => null, None

# print(datos.head())
# print(datos.head(10))

# print(datos.tail())
# print(datos.tail(3))

# print(datos.sample(3))

# print(datos)
# print(datos['TIPO_TRANSPORTE'])
# print(datos['TIPO_TRANSPORTE'].value_counts())