# import os
# archivo_contacto = None

# try:
#     #abrir de otra forma
#     with open('mis_archivos/contactos.txt','r') as archivo_contacto:
#         for linea in archivo_contacto:
#             print(linea.rstrip())
# except FileNotFoundError as e:
#     print("el archivo no existe",e)
# finally:
#     if archivo_contacto is not None:
#         archivo_contacto.close()

####atencion####
## OTRO EJERCICIO ## 
import os
from contacto import Contacto
archivo_contacto = None
lista_contacto = []

try:
    #
    with open('mis_archivos/contacto1.txt','r') as archivo_contacto:
        for linea in archivo_contacto:
            lista_split = linea.rstrip().split(";")
            contacto = Contacto()
            contacto.nombre = lista_split[0]
            contacto.apellido = lista_split[1]
            contacto.celular = lista_split[2]
            lista_contacto.append(contacto)

    for contacto in lista_contacto:
        print(contacto)

except FileNotFoundError as e:
    print("el archivo no existe",e)
finally:
    if archivo_contacto is not None:
        archivo_contacto.close()
