import numpy as np

def normal_equation():
    X   = np.random.normal(size=(20,20))
    x=X.transpose()
    y= np.random.randint(1000,size=(20,1),dtype= 'int32')
    adjoint= np.linalg.inv(x*X)
    theta= adjoint*x*y
    return theta
