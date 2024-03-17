import os

archivo_contacto = None
#leer archivos como bloques de informacion
try:
    with open('mis_archivos/contactos.txt') as archivo_contacto:
        archivo_contacto.seek(0)   
        #print(archivo_contacto.read(25))
        print(f'{archivo_contacto.read(20)} | {archivo_contacto.read(20)} | {archivo_contacto.read(11).rstrip()}')
        print(f'{archivo_contacto.read(20)} | {archivo_contacto.read(20)} | {archivo_contacto.read(11).rstrip()}')
except FileNotFoundError as e:
    print("el archivo no existe",e)
finally:
    if archivo_contacto is not None:
        archivo_contacto.close()
        