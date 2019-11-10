#Funciones del modelo constitutivo
import numpy as np


#Relacion entre tension deviatorica-deformacion axil
def sigdev(E,eps_a,sig_dev_u):
    #E: modulo de elasticidad del estrato
    #eps_a: deformacion xxx
    #sig_dev_u tension deviatorica ultima
    #dc_dev: tension deviatoria
    a=(1/E)
    b=(eps_a/sig_dev_u)
    sig_dev=eps_a/(a+b)
    return sig_dev

#Razon de falla: relacion entre tension de falla y ultima
def rf(sig_dev_f,sig_dev_u):
    #sig_dev_f tension deviatorica de falla
    #sig_dev_u tension deviatorica ultima
    Rf=sig_dev_f/sig_dev_u
    return Rf

#Fraccion de resistencia movilizada
def S(sig_dev,sig_dev_f):
    #sig_dev_f tension deviatorica de falla
    #sig_dev tension deviatorica
    S=sig_dev/sig_dev_f
    return S

#Modulo de elasticidad en funcion del confinamiento
def E_janbu(K,p_atm,sig3,n):
    #K y n: factores adimensionales a calibrar
    #p_atm: presion atmosferica
    #sig_3: presion de confinamiento
    E=K*p_atm*(sig3/p_atm)**n
    return E

#Nombre?
def Et(S,Rf,E):
    Et=((1-S*Rf)**2)*E
    return Et

#Tension de falla
def sig_dev_f(c,phi,sig3):
    #c: cohesion
    #phi: angulo de friccion interna
    #sig_3: presion de confinamiento
    phi_rad=np.radians(phi)
    sig_dev_f=(2*np.cos(phi_rad)+2*sig3*np.sin(phi_rad))/(1-np.sin(phi_rad))
    return sig_dev_f

#Distancia radian en donde la distorcion es despreciable
def rm(H,nu):
    rm=2*H*(1-nu)
    return rm

#