#!/usr/bin/python3
import sys, os, re #Se cargan las librerias

#Se declaran las variables, listas, tuplas, contadores, etc
file_name="" #Nombre del archivo
file_text="" #Contenido del archivo
text_split=[] #Contenido compactado
lista_text_split=[] #Lista de contenido compactado (registro en tuplas)
count=1 #Contador para la organizacion del texto
texto="" #Variable para almacenar el resultado final

#Se limpia la pantalla y cargan las interacciones con el usuario
os.system("clear")
print ("Mision 1: ")
print ("Leer archivo de texto separado por tabulaciones, ordenar los datos por nombre e imprimirlos con el siguiente formato:\n\n")

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

#Se recorre la lista ordenada para imprimir el contenido
#Primero recorre la lista, luego las tuplas
#Solo imprime las coincidencias segun el patron
for text_index in lista_text_split:
    patron = re.compile('^[AGMV]....*[aosz]$')
    coincidencia = patron.findall(text_index[1])
    #Si se haya una coincidencia recorre la tupla para imprimir el campo en el formato indicado (en caso de que este vacio no imprime nada)
    if len(coincidencia)>0:
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
