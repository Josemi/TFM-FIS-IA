# Versión 1.0 clase posición
# Autor: José Miguel Ramírez Sanz

#imports
import numpy as np
import math

#Clase de posición versión 1.0
class Posicion():
    
    # param x: lista con los valores del eje x de los puntos obtenidos con detectron
    #param y: lista con los valores del eje y de los puntos obtenidos con detectron
    def __init__(self,x,y):
        self.nariz = [x[0],y[0]]
        self.ojoI = [x[1],y[1]]
        self.ojoD = [x[2],y[2]]
        self.orejaI=[x[3],y[3]]
        self.orejaD=[x[4],y[4]]
        self.hombroI=[x[5],y[5]]
        self.hombroD=[x[6],y[6]]
        self.cuello = self.calcularPuntoMedio(self.hombroI,self.hombroD)
        self.angCuelloSupI = self.calcularAngulo(self.hombroI,self.cuello,self.nariz)
        self.angCuelloSupD = self.calcularAngulo(self.hombroD,self.cuello,self.nariz)
        self.codoI = [x[7],y[7]]
        self.codoD = [x[8],y[8]]
        self.manoI=[x[9],y[9]]
        self.manoD = [x[10],y[10]]
        self.yD = ((self.codoD[1]-self.hombroD[1])*(self.manoD[0]-self.hombroD[0])/(self.codoD[0]-self.hombroD[0]))+self.hombroD[1]
        self.angCodoI = self.calcularAngulo(self.hombroI,self.codoI,self.manoI)
        self.angCodoD = self.calcularAngulo(self.hombroD,self.codoD,self.manoD)
        self.angHombroI = self.calcularAngulo(self.cuello,self.hombroI,self.codoI)
        self.angHombroD = self.calcularAngulo(self.cuello,self.hombroD,self.codoD)
        self.caderaI = [x[11],y[11]]
        self.caderaD = [x[12],y[12]]
        self.cadera = self.calcularPuntoMedio(self.caderaI,self.caderaD)
        self.angCuelloInfI =self.calcularAngulo(self.hombroI,self.cuello,self.cadera)
        self.angCuelloInfD =self.calcularAngulo(self.hombroD,self.cuello,self.cadera)
        self.rodillaI = [x[13],y[13]]
        self.rodillaD = [x[14],y[14]]
        self.angCaderaI = self.calcularAngulo(self.cadera,self.caderaI,self.rodillaI)
        self.angCaderaD = self.calcularAngulo(self.cadera,self.caderaD,self.rodillaD)
        self.angCaderaTorsoI = self.calcularAngulo(self.cuello,self.cadera,self.caderaI)
        self.angCaderaTorsoD = self.calcularAngulo(self.cuello,self.cadera,self.caderaD)
        self.tobilloI = [x[15],y[15]]
        self.tobilloD = [x[16],y[16]]
        self.angRodillaI = self.calcularAngulo(self.caderaI,self.rodillaI,self.tobilloI)
        self.angRodillaD = self.calcularAngulo(self.caderaD,self.rodillaD,self.tobilloD)
        self.distAntebrazoI = self.calcularDistancia(self.manoI,self.codoI)
        self.distAntebrazoD = self.calcularDistancia(self.manoD,self.codoD)
        self.distBrazoI = self.calcularDistancia(self.codoI,self.hombroI)
        self.distBrazoD = self.calcularDistancia(self.codoD,self.hombroD)
        self.distCuello = self.calcularDistancia(self.nariz,self.cuello)
        self.distTronco = self.calcularDistancia(self.cuello,self.cadera)
        self.distMusloI = self.calcularDistancia(self.caderaI,self.rodillaI)
        self.distMusloD = self.calcularDistancia(self.caderaD,self.rodillaD)
        self.distPiernaI = self.calcularDistancia(self.rodillaI,self.tobilloI)
        self.distPiernaD = self.calcularDistancia(self.rodillaD,self.tobilloD)
        self.distHombros = self.calcularDistancia(self.hombroI,self.hombroD)
        self.distCadera = self.calcularDistancia(self.caderaI,self.caderaD)
    
    #Función que permite calcular el punto medio entre dos puntos
    #param p1: punto 1
    #param p2: punto 2
    #return: punto medio entre los dos puntos
    def calcularPuntoMedio(self,p1,p2):
        return [(p1[0]+p2[0])/2,(p1[1]+p2[1])/2]
    
    #Función que devuelve el ángulo entre 3 puntos dados
    #param p1: punto 1
    #param p2: punto medio entre el punto 1 y 3
    #param p3: punto 3
    #return: ángulo en 180 grados
    def calcularAngulo(self,p1,p2,p3):
        v1 = self.calcularVector(p1,p2)
        v2 = self.calcularVector(p3,p2)
        uv1 = v1 / np.linalg.norm(v1)
        uv2 = v2 / np.linalg.norm(v2)
        dp = np.dot(uv1, uv2)
        return math.degrees(np.arccos(dp))
    
    #Función que permite calcular el vector entre dos puntos
    #param p1: punt 1
    #param p2: punto 2
    #return: vector que une los dos puntos
    def calcularVector(self,p1,p2):
        return [p2[0]-p1[0],p2[1]-p1[1]]
    
    #Función que permite calcular la distancia entre dos puntos
    #param p1: punto 1
    #param p2: punto 2
    #return: distancia euclídea entre los dos puntos
    def calcularDistancia(self,p1,p2):
        return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5
    
    #Función que devuelve todos los ángulos para su posterior comparación
    #return: lista con todos los valores de los ángulos obtenidos en la clase
    def devuelveAngulos(self):
        return [self.angCuelloSupI,self.angCuelloSupD,self.angCodoI,self.angCodoD,self.angHombroI,self.angHombroD,
               self.angCuelloInfI,self.angCuelloInfD,self.angCaderaI,self.angCaderaD,self.angRodillaI,self.angRodillaD,
               self.angCaderaTorsoI,self.angCaderaTorsoD]