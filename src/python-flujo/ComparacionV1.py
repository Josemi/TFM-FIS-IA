# Versión 1.0 comparación de posiciones
# Esta es la versión inicial que solo se usó como prueba
# Autor: José Miguel Ramírez Sanz

#Función que permite comparar dos posiciones
#param pos1: posición 1
#param pos2: posición 2
def comparaPosiciones(pos1,pos2):
    res=0.0
    ang1 = pos1.devuelveAngulos()
    ang2 = pos2.devuelveAngulos()
    for i in range(len(ang1)):
        res+= abs(ang1[i]-ang2[i])
    return res