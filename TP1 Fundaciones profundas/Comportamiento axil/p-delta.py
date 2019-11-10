import numpy as np
import matplotlib.pyplot as plt



def Pf_func(d,Kf,Rf,f):
    
    a=1/Kf
    b=Rf*d/f
    Pf=d/(a+b)
    return Pf

def Pp_func(d,Kp,Rf,Qpv):
    a=1/Kp
    b=Rf*d/Qpv
    Pp=d/(a+b)
    return Pp


Kf=1
Rf=0.5
f=0.3
Kp=1
Qpv=10

d=np.linspace(0, 10, num=20)   
Pf=np.zeros(20)
Pp=np.zeros(20)
P=np.zeros(20)
for i in range(len(d)):
    
    d_i=d[i]
    Pf_i=Pf_func(d_i,Kf,Rf,f)
    Pp_i=Pp_func(d_i,Kf,Rf,Qpv)
    P_i=Pf_i+Pp_i
    
    Pf[i]=Pf_i
    Pp[i]=Pp_i
    P[i]=P_i
    
    
plt.plot(d,Pf)
plt.show()
plt.plot(d,Pp)
plt.show()
plt.plot(d,P)
plt.show()
    
