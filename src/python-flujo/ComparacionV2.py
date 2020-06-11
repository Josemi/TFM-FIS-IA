# Versión 2.0 comparación de posiciones
# Autor: José Miguel Ramírez Sanz

#Función que permite comparar los brazos de dos posiciones y penalizar si fuera necesarto
#param pos1: posición 1
#param pos2: posición 2
#param penalizacionCodo: penalización que se aplicaría por fallo en los codos
#param penalizacionHombro: penalización que se aplicaría por fallo en los hombros
#param diferenciaEstirado: grados de diferencia para considerar o no que el ángulo es 180 grados
#return: diferencia entre brazos
def compararBrazos(pos1,pos2,penalizacionCodo = 180,penalizacionHombro=90, diferenciaEstirado=10):
    partes=["D","I"]
    res=0.0
    pos=[pos1,pos2]
    
    for j in partes:
        res+= abs(eval("pos1.angCodo"+j)-eval("pos2.angCodo"+j))
        res+= abs(eval("pos1.angHombro"+j)-eval("pos2.angHombro"+j))
        auxCodo = []
        auxHombro = []
        for i in pos:
            
            #Si el brazo está estirado
            if  180-diferenciaEstirado <= eval("i.angCodo"+j) <= 180+diferenciaEstirado:
                auxCodo.append(0)
            #Si no está estirado
            else:
                if eval("i.mano"+j+"[1]") > eval("i.codo"+j+"[1]"):
                    auxCodo.append(1)
                else: 
                    auxCodo.append(2)
            
            # Si el angulo del hombro es casi 180 entonces 0
            if  180-diferenciaEstirado <= eval("i.angHombro"+j) <= 180+diferenciaEstirado:
                auxHombro.append(0)
            #Sino comparar si está hacia arriba o hacia abajo
            else:
                if eval("i.codo"+j+"[1]") > eval("i.hombro"+j+"[1]"):
                    auxHombro.append(1)
                else:
                    auxHombro.append(2)
                    
        if (auxCodo[0] == 1 and  auxCodo[1]==2) or (auxCodo[0] == 2 and  auxCodo[1]==1):
            res+=penalizacionCodo
            print("Penalizado brazo " + j)
        if (auxHombro[0] == 1 and  auxHombro[1]==2) or (auxHombro[0] == 2 and  auxHombro[1]==1):
            res+=penalizacionHombro
            print("Penalizado hombro " + j)
    return res

#Función que permite comparar los brazos de dos posiciones y penalizar si fuera necesarto
#param pos1: posición 1
#param pos2: posición 2
#param penalizacionCodo: penalización que se aplicaría por fallo en los codos u hombros
#param diferenciaPena: diferencia para designar si una brazo está al mismo nivel (0), está arriba (1) o abajo del codo (2)
#return: diferencia entre brazos
def compararBrazosV1(pos1,pos2,penalizacion = 100,diferenciaPena = 5):
    res=0.0
    
    res+= abs(pos1.angCodoD-pos2.angCodoD)
    bD1 = 0
    
    #Si la diferencia de altura es superior a la establecida se comprueba si está por encima o por debajo
    if abs(pos1.manoD[1]*100/pos1.codoD[1]-100)>diferenciaPena:
        if pos1.manoD[1] > pos1.codoD[1]:
            bD1 = 1
        else: 
            bD1 = 2
    bD2 = 0
    if abs(pos2.manoD[1]*100/pos2.codoD[1]-100)>diferenciaPena:
        if pos2.manoD[1] > pos2.codoD[1]:
            bD2 = 1
        else: 
            bD2 = 2
    #Penalizamos
    if (bD1 == 1 and  bD2==2) or (bD1 == 2 and  bD2==1):
        res+=penalizacion
        print("Penalizado brazo derecho")
    
    res+= abs(pos1.angCodoI-pos2.angCodoI)
    
    bI1 = 0
    if abs(pos1.manoI[1]*100/pos1.codoI[1]-100)>diferenciaPena:
        if pos1.manoI[1] > pos1.codoI[1]:
            bI1 = 1
        else: 
            bI1 = 2
    bI2 = 0
    if abs(pos2.manoI[1]*100/pos2.codoI[1]-100)>diferenciaPena:
        if pos2.manoI[1] > pos2.codoI[1]:
            bI2 = 1
        else: 
            bI2 = 2
    #Penalizamos
    if (bI1 == 1 and  bI2==2) or (bI1 == 2 and  bI2==1):
        res+=penalizacion
        print("Penalizado brazo izquierdo")
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
    zonas=["angCaderaTorso","angCuelloSup"]
    res = 0.0
    for i in partes:
        for j in zonas:
            res+=abs(eval("pos1."+j+i)-eval("pos2."+j+i))
    return res

#Función que permite obtener la comparación entre dos posiciones dando pesos a las distintas partes
#param pos1: posición 1
#param pos2: posición 2
#param penalizacionCodo: penalización que se aplicaría por fallo en los codos
#param penalizacionHombro: penalización que se aplicaría por fallo en los hombros
#param diferenciaEstirado: grados de diferencia para considerar o no que el ángulo es 180 grados
#param pesoBrazos: peso que se le quiere dar a los brazos
#param pesoPiernas: peso que se le quiere dar a las piernas
#param pesoTors: peso que se le quiere dar al torso
#return: resultado de la diferencia
def compararPosiciones(pos1,pos2,penalizacionCodo = 180,penalizacionHombro=90,diferenciaEstirado = 10,pesoBrazos=1,pesoPiernas=1,pesoTorso=1):
    return pesoBrazos*compararBrazos(pos1,pos2,penalizacion,diferenciaEstirado)+pesoPiernas*compararPiernas(pos1,pos2)+pesoTorso*compararTorso(pos1,pos2)