from pyswip import Prolog
prolog = Prolog()
prolog.consult("/hechos.pl")
print("__________")
print("PROYECTO PROGRAMACION LOGICA Y FUNCIONAL")
print("SISTEMA EXPERTO PARA VERIFICAR LA PROBABILIDAD DE APROBAR PROGRAMACION LOGICA")
print("__________")

p = False
while not p:
    
    for valor in prolog.query("proba(X,logica)"):
        print (' TIENE PROBABILIDADES DE APROBAR LOGICA => ', valor ["X"])

    for valor in prolog.query("pronoaprobar(X,logica)"):
        print (' NO TIENE PROBAILIDADES PARA APROBAR LOGICA => ', valor ["X"])
        
    X= input("__________\nTEMA 1\n__________\nESCRIBA EL NOMBRE DEL ALUMNO ")

    for valor in prolog.query("puntuacionT1("+X+ ", Y)"):
        print (X,' OBTUVO LA CALIFICACION : ', valor ["Y"],"¡¡USTED TIENE QUE ESTUDIAR MAS ESTE TEMA!!")

    X= input("__________\nTEMA 2\n__________\nESCRIBA EL NOMBRE DEL ALUMNO")

    for valor in prolog.query("puntuacionT2("+X+ ", Y)"):
        print (X,' OBTUVO LA CALIFICACION : ', valor ["Y"],"¡¡USTED DEBERIA ESTUDIAR MAS!!")    
    
    for valor in prolog.query("probaprobar(X,logica)"):
        print (' ESTOS SON LOS LOS APROBADOS DE LA MATERIA : ', valor ["X"]+" !MUCHAS FELICIDADES¡")

    for valor in prolog.query("probnoaprobar(X,logica)"):
        print (' ESTOS SON LOS NO APROBADOS ', valor ["X"]+" ESTUDIAR +LOGICA")

    l = input('¿QUIERE SALIR DEL SISTEMA?\n0-YES  1-NO')
    p = l.lower() in ['0']
    if p:
        print("Sistema probabilistico aprobar logica")
        print("Programacion lofica funcional, FIN DEL SISTEMA)
        