import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("datasetp3.csv") #<----Please mention file path in quotes here if Spyder IDE is not used

x= data.age
y= data.charges

x = np.row_stack(x)
y = np.row_stack(y)
X = [x,y]

xbar = x.mean()
ybar = y.mean()

def cov(x,y):
    xbar, ybar = x.mean(), y.mean()
    return np.sum((x-xbar)*((y-ybar).T))/(len(x)-1)

def cov_mat(X):
    Cmat= np.array([[cov(X[0],X[0]), cov(X[0], X[1])], 
             [cov(X[1],X[0]), cov(X[1],X[1])]])
    return Cmat

A = cov_mat(X)

def calc_SVD(A):
    AT= A.T
    ATA= AT.dot(A)
    eigval_U, eigvec_U = np.linalg.eig(ATA)
    sort_eigval_U =  eigval_U.argsort()[::-1] #sorted eigenvalues of eigval_U
    U = eigvec_U[:, sort_eigval_U]
    H = U[:,1]
    return H

B = calc_SVD(A)
d = B[0]*xbar + B[1]*ybar
line = (d - (B[0]*x))/B[1]

plt.scatter(x,y) #Data plot
plt.plot(x, line, 'y-')
plt.show
