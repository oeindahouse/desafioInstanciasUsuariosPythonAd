import os

archivo_contacto = None
tamano_bloque_bytes = 50

try:
    with open('mis_archivos/contactos.txt','rb') as archivo_contacto:
        bloque = archivo_contacto.read(tamano_bloque_bytes)
        
        while bloque:
            print(bloque)
            bloque = archivo_contacto.read(tamano_bloque_bytes)
        
        
        
#         print(f'{archivo_contacto.read(20)} | {archivo_contacto.read(20)} | {archivo_contacto.read(10).rstrip()}')
#         archivo_contacto.seek(50) 
#         print(f'{archivo_contacto.read(20)} | {archivo_contacto.read(20)} | {archivo_contacto.read(10).rstrip()}')
except FileNotFoundError as e:
    print("el archivo no existe",e)
finally:
    if archivo_contacto is not None:
        archivo_contacto.close()
        