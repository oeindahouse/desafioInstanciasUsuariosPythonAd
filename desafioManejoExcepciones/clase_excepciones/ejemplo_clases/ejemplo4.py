import os

archivo_log = None

if not os.path.exists("logs"):
    os.mkdir("logs")
    


    
    
archivo_log = open("logs/error.log",'w')
#archivo_log = open("2024-03-13.log",'w'
archivo_log.close()

antiguo = os.path.join('logs','error.log') #logserrpr.txt
nuevo = os.path.join('logs', 'error.txt') #logs/error.log
print(antiguo, nuevo)

os.rename(antiguo, nuevo)


REVISAR
