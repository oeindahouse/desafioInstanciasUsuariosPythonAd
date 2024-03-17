import os
#scrip para modificar nombre
archivo_log = None
if not os.path.exists("logs"):
    os.mkdir("logs")

#recordar que el ejecutar el codigo, se debe cambiar
#el nombre del archivo aqui abajo y en nuevo, xq no se puede cambiar algo por 
#el mismo en este caso    
archivo_log = open("logs/error.log","w")
archivo_log.close()

#join me entrega una ruta como lo que esta en el #
antiguo = os.path.join('logs','error.log') #logs/error.log
nuevo = os.path.join('logs','error.txt') #logs/error.txt
print(antiguo, nuevo)

os.rename(antiguo,nuevo)

    
#if archivo_log is not None:
#    archivo_log.close()