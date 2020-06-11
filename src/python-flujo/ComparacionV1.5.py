# Versión 1.5 comparación de posiciones
# Esta es la verdadera versión 1 de la comparación, la versión 1.0 es más una prueba
# Autor: José Miguel Ramírez Sanz

#Función que permite comparar los brazos
#param pos1: posición 1
#para pos2: posición 2 
#return: resultado de la diferencia
def compararBrazos(pos1,po2):
    partes = ["D","I"]
    zonas = ["angCodo"]
    res = 0.0
    for i in partes:
        for j in zonas:
            res+=abs(eval("pos1."+j+i)-eval("pos2."+j+i))
    return res

#Función que permite comparar las piernas
#param pos1: posición 1
#para pos2: posición 2
#return: resultado de la diferencia
def compararPiernas(pos1,pos2):
    partes = ["D","I"]
    zonas = ["angRodilla","angCadera"]
    res = 0.0
    for i in partes:
        for j in zonas:
            res+=abs(eval("pos1."+j+i)-eval("pos2."+j+i))
    return res

#Función que permite comparar el torso
#param pos1: posición 1
#para pos2: posición 2
#return: resultado de la diferencia
def compararTorso(pos1,pos2):
    partes=["D","I"]
    zonas=["angCaderaTorso","angHombro","angCuelloSup"]
    res = 0.0
    for i in partes:
        for j in zonas:
            res+=abs(eval("pos1."+j+i)-eval("pos2."+j+i))
    return res

#Función que permite obtener la comparación entre dos posiciones dando pesos a las distintas partes
#param pos1: posición 1
#param pos2: posición 2
#param pesoBrazos: peso que se le quiere dar a los brazos
#param pesoPiernas: peso que se le quiere dar a las piernas
#param pesoTors: peso que se le quiere dar al torso
#return: resultado de la diferencia
def compararPosiciones2(pos1,pos2,pesoBrazos=1,pesoPiernas=1,pesoTorso=1):
    return pesoBrazos*compararBrazos(pos1,pos2)+pesoPiernas*compararPiernas(pos1,pos2)+pesoTorso*compararTorso(pos1,pos2)