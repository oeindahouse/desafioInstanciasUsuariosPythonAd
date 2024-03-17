import json
from usuario import Usuario
from datetime import datetime


def cinstancia_user(linea):
    try:
        log = None
        datos_usuario = json.loads(linea)
        usuario = Usuario(datos_usuario["nombre"], datos_usuario["apellido"], datos_usuario["email"], datos_usuario["genero"])
        return usuario
    except Exception as e:
        fecha_actual = datetime.now()
        with open(f'{str(fecha_actual).split(" ")[0]}.log', 'a') as log:
            log.write(f'{fecha_actual} - [ERROR]: {e}\n')
    finally:
        if log is not None:
            log.close()
    

        
        


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

def info_personas():
    lista_usuarios = []
    with open('desafio/usuarios.txt', 'r') as listado_personal:
        for linea in listado_personal:
            usuario = cinstancia_user(linea.strip())
            if usuario:
                lista_usuarios.append(usuario)
    
    print(" usuarios cargados:")
    for usuario in lista_usuarios:
        print(usuario.__dict__)

