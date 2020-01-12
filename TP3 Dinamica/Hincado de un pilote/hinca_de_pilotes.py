#Hinca dinamica de plilotes y tablestacas

#Propiedades del pilote y suelo
lpilote=3.048
k=0.
c=0.
K=1e32
C=0.
E=47896. #modulo de elasticidad
gammas=20.27 #peso especifico
ro=gammas/9.807 #densidad
A=1. #area transversal del elemento
S=1.257 #perimetro del elemento

#Discretizacion por FEM
nelem=500 #numero de elementos finitos
li=lpilote/nelem #longitud de cada elemento
nnodelem=2 #numero de nodos por elemento
nnod=nelem+1 #numero de nodos globales
npg=2 #numero de puntos de gauss

#Rutina para puntos y pesos de Gauss (descargada y traducida de Mathworks)
