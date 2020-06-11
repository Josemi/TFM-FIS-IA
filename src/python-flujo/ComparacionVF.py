# Versión 4.0 comparación de posiciones, versión final
# Autor: José Miguel Ramírez Sanz

#Función que devuelve la diferencia media en grados y en porcentaje entre los posiciones atendiendo a uno pesos por cada zona
#param pos1: posición 1
#param pos2: posición 2
#param pesos: diccionario con los pesos de las distintas zonas
#return: diferencia media en grados, porcentaje de exactitud
def compararPosiciones(pos1,pos2,pesos={"brazos":1,"piernas":1,"torso":1}):
    zonas={"brazos":["angCodo","angHombro"],"piernas":["angRodilla","angCadera"],"torso":["angCaderaTorso","angCuelloSup"]}
    res=0
    total=0
    
    #Se recoge el peso total
    for i in pesos:
        if i not in zonas:
            raise Exception("No se puede dar peso a una zona que no esté definida")
        total+=pesos[i]
        
    #Se recorren los distintos tipos de zonas y se les aplica el peso a la comparación
    for i in zonas:
        res+=(pesos[i]/total)*comparacionZona(pos1,pos2,zonas[i])
    
    porcentaje = res*100/180
    
    return res,100-porcentaje

#Función que permite comparar unas zonas pasadas
#param pos1: posición 1
#param pos2: posición 2
#param zonas: lista de las zonas a comparar
#return: media de la diferencia de los grados de las zonas pasadas
def comparacionZona(pos1,pos2,zonas):
    partes=["D","I"]
    res = 0.0
    for i in partes:
        for j in zonas:
            #aux es la diferencia entre los ángulos
            aux = abs(eval("pos1."+j+i)-eval("pos2."+j+i))
            #si la diferencia es mayor de 180 grados se coge el otro lado
            if aux > 180:
                res += (360-aux)
            else:
                res+=aux
    return res/(len(partes)*len(zonas))