import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv("datasetp3.csv") #<----Please mention file path in quotes here if Spyder IDE is not used

x= data.age
y= data.charges
X= np.column_stack([x, y])

#To find covariances of a matrix
def cov(x,y):
    xbar, ybar = x.mean(), y.mean()
    return np.sum((x-xbar)*((y-ybar).T))/(len(x)-1)

#Covariance matrix
def cov_mat(X):
    Cmat= np.array([[cov(X[0],X[0]), cov(X[0], X[1])], 
             [cov(X[1],X[0]), cov(X[1],X[1])]])
    return Cmat
#covi = np.cov(x,y)
eigval, eigvec = np.linalg.eig(cov_mat(X))

print('The Eigen values of the Matrix X:')
print(eigval)

print('The Corresponding Eigen vectors of X:')
print(eigvec)

O = [x.mean(),y.mean()]
s_eigvec = eigvec[:,0]
l_eigvec = eigvec[:,1]

#calculate Covariance matrix
print('The Covariance Matrix:')
print(cov_mat(X))


#print(covi)
plt.scatter(x,y)
plt.quiver(*O, *s_eigvec, color=['r'], scale=6) #Eigenvector X
plt.quiver(*O, *l_eigvec, color=['b'], scale=6) #Eigenvector Y
plt.show







