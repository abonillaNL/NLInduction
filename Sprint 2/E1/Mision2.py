#!/usr/bin/python3
import sys, os #Se cargan las librerias

#Se declaran las variables, listas, tuplas, contadores, etc
file_name="" #Nombre del archivo
file_text="" #Contenido del archivo
text_split=[] #Contenido compactado
lista_text_split=[] #Lista de contenido compactado (registro en tuplas)
count=1 #Contador para la organizacion del texto
texto="" #Variable para almacenar el resultado final

#Se limpia la pantalla y cargan las interacciones con el usuario
os.system("clear")
print ("Mision 2: ")
print ("Mismos requerimientos que Mision 1, debe imprimir solo las lineas con apellidos de mas de 5 caracteres:\n\n")

#Se comprueba que el nombre no este vacio 
if len(sys.argv) > 1:
    file_name = sys.argv[1]
else:
    print ("Sintaxis: ./comando archivo")
    print ("El nombre no puede estar vacio.")
    sys.exit()

#Se intenta abrir el archivo para lectura (si existe)
try:
    file = open(file_name, "r")
except IOError:
    print ("No se pudo leer correctamente el archivo", file_name)
    sys.exit()

#Se guarda el contenido del archivo en una variable y se cierra el mismo
file_text = file.read()
file.close

#Se organiza el archivo (Primero se quitan los saltos de linea y vacía el primer campo)
text_split = file_text.split('\n')
text_split[0]=""

#Se borran los campos vacios
text_split = [item for item in text_split if item]

'''
    Como quedaría el contenido sin quitar el tabulador
    ['Pepe            Pepito              XXXXXXX',
    'Jose            Algo                ZZZZZZZ',
    'María           Nose                HHHHHHH']

'''

#Se guarda el contenido limpiado en una tupla y esta en una lista
#(el for recorre cada elemento para limpiarlo de tabuladores antes de almacenarlo en la lista)
for text_index in text_split:
    text_split = text_index.split()
    text_split = tuple(text_split)
    lista_text_split.append(text_split)
    
'''
    Asi queda luego del for:
    [
        ('Pepe', 'Pepito', 'XXXXXXX'),
        ('Jose', 'Algo', 'ZZZZZZZ'),
        ('María', 'Nose', 'HHHHHHH')
    ]
'''

#Se ordena la lista segun la primera linea
lista_text_split=sorted(lista_text_split)

#Primero recorre la lista
for text_index in lista_text_split:
    #Comprueba que el largo del apellido sea mayor a 5 caracteres
    if len(text_index[1])>5:
        #Si lo es, recorre las tuplas para imprimir la linea
        for index in text_index:
            if count != len(text_index):
                if count == 1:
                    texto=index
                else:
                    texto=texto+"-"+index
                count=count+1
            else:
                texto=texto+"-"+index
                print(texto.strip())
                texto=""
                count=1
    else:
        #Si el apellido es menor o igual a 5 caracteres oculta la linea
        print(end='')
