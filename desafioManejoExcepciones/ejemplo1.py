import os
archivo_contacto = None
#abrir archivo
try:
    print(os.path.abspath('mis_archivos/contactos.txt'))
    archivo_contacto = open(os.path.abspath('mis_archivos/contactos.txt'))
except FileNotFoundError as e:
    print("el archivo no existe",e)
finally:
    if archivo_contacto is not None:
        archivo_contacto.close()