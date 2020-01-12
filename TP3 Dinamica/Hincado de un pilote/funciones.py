#Jacobiano de la matrix de funciones de forma
def dh(vpg,dim,nnodelem):
    delta=1e-6
    mdelta=delta*np.eye(dim)
    DH=np.zeros((dim,nnodelem))
    #for i in range(dim):
    #    for j in range(nnodelem):
            #DH[i,j]=1/(2*delta)*(h(vpg+mdelta[i,j])-h(vpg-mdelta[i,j]))
    return DH

#Funcion de forma
def h(vpg):
    
    r=vpg
    h1=0.5*(1+r)
    h2=0.5*(1-r)
    H=np.array([h1,h2])
    return H

#Derivada de las funciones de forma respecto a la configuracion de referencia
def h0(vpg,dim,nnodelem):
    H0=invJ(vpg)*dh(vpg,dim,nnodelem)
    return H0
    
#Matriz jacobiana inversa
def invJ(vpg,dim):
    a=np.eye(dim)
    b=Jac(vpg)
    iJ=np.linalg.solve(a, b)
    return iJ
    
#Matriz jacobiana
def Jac(vpg,dim,nnodelem,mcoor):
    J=dh(vpg,dim,nnodelem)*mcoor
    return J

import numpy as np    
#


