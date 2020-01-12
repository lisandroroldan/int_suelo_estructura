def lgwt(N):
    import numpy as np
    
    N=N-1
    N1=N+1
    N2=N+2
    
    xu=np.linspace(-1.,1.,N1)
    nv=np.linspace(0.,N,N+1)
    
    #Initial guess
    y=np.cos((2*nv+1)*np.pi/(2*N+2))+(0.27/N1)*np.sin(np.pi*xu*N/N2)
    
    #Legendre-Gauss Vandermonde Matrix
    L=np.zeros((N1,N2))
    
    #Derivative of LGVM
    Lp=np.zeros((N1,N2));
    
    #Compute the zeros of the N+1 Legendre Polynomial
    #using the recursion relation and the Newton-Rhapson method
    y0=2
    
    #Iterate until new points are uniformly within epsilon of old points
    while np.max(np.abs(y-y0))>np.spacing(1):
        L[:,0]=1
        Lp[:,0]=0
        
        L[:,1]=y
        Lp[:,1]=1
        
        
    
    return L,y

print(lgwt(2))

