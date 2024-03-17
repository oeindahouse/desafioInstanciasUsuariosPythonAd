from datetime import datetime
log = None

try:
    edad = int(input("ingrese la edad: "))
    
    
except Exception as e:
    fecha_actual = datetime.now()
    with open(f'{str(fecha_actual).split(" ")[0]}.log','a') as log:
        log.write(f'{fecha_actual} - [error]: {e}\n')
        
finally:
    if log is not None:
        log.close()
        
    