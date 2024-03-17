import os

archivo_contacto = None

try:
    with open('mis_archivos/contactos.txt') as archivo_contacto:
        archivo_contacto.seek(0)
        print(f'{archivo_contacto.read(11)} | {archivo_contacto.read(11)} | {archivo_contacto.read(9)}')
        archivo_contacto.seek(40)
        print(f'{archivo_contacto.read(11)} | {archivo_contacto.read(11)} | {archivo_contacto.read(9)}')

except FileNotFoundError as e:
    print("el archivo no existe", e)
finally:
    if archivo_contacto is not None:
        archivo_contacto.close()
        