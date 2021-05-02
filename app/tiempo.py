import time

def calcular_tiempo(tiempo):
    horas = int(tiempo/3600)
    minutos = int((tiempo%3600)/60)
    segundos = int(tiempo%60)
    tiempo = str(horas)+":"+str(minutos)+":"+str(segundos)
    return tiempo
