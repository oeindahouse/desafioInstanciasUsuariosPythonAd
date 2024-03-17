from datetime import datetime
log = None

#ingresar datos
try:
    edad = int(input("ingrese la edad: "))

except Exception as e:
    fecha_actual = datetime.now()
    #si en vez de ocupar a | utilizo w se borra el archivo log y empieza denuevo | si ocupo r arroja error, porque estoy tratando de escribir algo que solo se puede leer |
    #, si ocupo r+ falla si el archivo no existe
    with open(f'{str(fecha_actual).split(" ")[0]}.log', 'a') as log:
        log.write(f'{fecha_actual} - [ERROR]: {e}\n')
finally:
    if log is not None:
        log.close()