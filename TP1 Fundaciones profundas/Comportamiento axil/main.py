import numpy as np
import matplotlib.pyplot as plt
import duncan_chang as dc

#Parametros de Duncan y Chang para una arena silicea densa

Ke=2000
Ku=2120
n=0.54
Rf=0.91
c=0
phi=36.5
nu=0.32

print(dc.sig_dev_f(c,phi,0))