import numpy as np

def natural(N):
    w=[0 for j in range(N)]
    for i in range(N):
        w[i]=1/np.sqrt(2*np.pi)*np.exp(-((i-N/2))**2/(2))
    return w
def uniform(N,g):
    w = np.zeros([N])
    for i in range(N):
        w[i]=(i-(N/2))
    for i in range(N):
        if np.abs(w[i])>g:
            w[i]=0
        else:
            w[i]=1/(2*g)
    return w