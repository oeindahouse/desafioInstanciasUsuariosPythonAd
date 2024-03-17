import os
archivo_contacto = None
##abrir de otra forma
try:
    with open('mis_archivos/contactos.txt','r') as archivo_contacto:
        for linea in archivo_contacto:
            print(linea.rstrip())
               
    
except FileNotFoundError as e:
    print("el archivo no existe",e)
finally:
    if archivo_contacto is not None:
        archivo_contacto.close()
        
