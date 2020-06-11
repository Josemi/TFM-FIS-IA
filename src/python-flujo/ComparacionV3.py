# Versión 3.0 comparación de posiciones
# Autor: José Miguel Ramírez Sanz

#Función que permite comparar los brazos de dos posiciones y penalizar si fuera necesarto
#param pos1: posición 1
#param pos2: posición 2
#param penalizacionCodo: penalización que se aplicaría por fallo en los codos
#param penalizacionHombro: penalización que se aplicaría por fallo en los hombros
#param diferenciaEstirado: grados de diferencia para considerar o no que el ángulo es 180 grados
#return: diferencia media entre brazos
def compararBrazos(pos1,pos2,penalizacionCodo = 180,penalizacionHombro=90, diferenciaEstirado=10):
    partes=["D","I"]
    res=0.0
    pos=[pos1,pos2]
    
    for j in partes:
        res+= abs(eval("pos1.angCodo"+j)-eval("pos2.angCodo"+j))
        res+= abs(eval("pos1.angHombro"+j)-eval("pos2.angHombro"+j))
        auxCodoAltura = []
        auxCodoAnchura = []
        auxHombro = []
        for i in pos:
            
            #Si el brazo está estirado
            if  180-diferenciaEstirado <= eval("i.angCodo"+j) <= 180:
                auxCodoAltura.append(0)
            #Si no está estirado
            else:
                if eval("i.mano"+j+"[1]") > eval("i.codo"+j+"[1]"):
                    auxCodoAltura.append(1)
                else: 
                    auxCodoAltura.append(2)
                if eval("i.mano"+j+"[0]") > eval("i.codo"+j+"[0]"):
                    aux
            
            # Si el angulo del hombro es casi 180 entonces 0
            if  180-diferenciaEstirado <= eval("i.angHombro"+j) <= 180:
                auxHombro.append(0)
            #Sino comparar si está hacia arriba o hacia abajo
            else:
                if eval("i.codo"+j+"[1]") > eval("i.hombro"+j+"[1]"):
                    auxHombro.append(1)
                else:
                    auxHombro.append(2)
                    
        if (auxCodoAltura[0] == 1 and  auxCodoAltura[1]==2) or (auxCodoAltura[0] == 2 and  auxCodoAltura[1]==1):
            #Están a alturas distintas, comprobar si están en anchos distintos
            if (auxCodoAltura[0] == 1 and  auxCodoAltura[1]==2) or (auxCodoAltura[0] == 2 and  auxCodoAltura[1]==1):
                res+=penalizacionCodo
                print("Penalizado codo " + j)
        if (auxHombro[0] == 1 and  auxHombro[1]==2) or (auxHombro[0] == 2 and  auxHombro[1]==1):
            res+=penalizacionHombro
            print("Penalizado hombro " + j)
    return res/(len(pos)*len(partes))

#Función que permite comparar las piernas
#param pos1: posición 1
#para pos2: posición 2
#return: resultado medio de la diferencia
def compararPiernas(pos1,pos2):
    partes = ["D","I"]
    zonas = ["angRodilla","angCadera"]
    res = 0.0
    for i in partes:
        for j in zonas:
            res+=abs(eval("pos1."+j+i)-eval("pos2."+j+i))
    return res/(len(zonas)*len(partes))

#Función que permite comparar el torso
#param pos1: posición 1
#para pos2: posición 2
#return: resultado medio de la diferencia
def compararTorso(pos1,pos2):
    partes=["D","I"]
    zonas=["angCaderaTorso","angCuelloSup"]
    res = 0.0
    for i in partes:
        for j in zonas:
            res+=abs(eval("pos1."+j+i)-eval("pos2."+j+i))
    return res/(len(zonas)*len(partes))

#Función que permite obtener la comparación entre dos posiciones dando pesos a las distintas partes
#param pos1: posición 1
#param pos2: posición 2
#param penalizacionCodo: penalización que se aplicaría por fallo en los codos
#param penalizacionHombro: penalización que se aplicaría por fallo en los hombros
#param diferenciaEstirado: grados de diferencia para considerar o no que el ángulo es 180 grados
#param pesoBrazos: peso que se le quiere dar a los brazos
#param pesoPiernas: peso que se le quiere dar a las piernas
#param pesoTors: peso que se le quiere dar al torso
#return: resultado medio de la diferencia
def compararPosiciones(pos1,pos2,penalizacionCodo = 180,penalizacionHombro=90,diferenciaEstirado = 10,pesoBrazos=1,pesoPiernas=1,pesoTorso=1):
    total = pesoBrazos+pesoPiernas+pesoTorso
    return (pesoBrazos/total)*compararBrazos(pos1,pos2,penalizacionCodo,penalizacionHombro,diferenciaEstirado)+(pesoPiernas/total)*compararPiernas(pos1,pos2)+(pesoTorso/total)*compararTorso(pos1,pos2)