#Librarures that are imported
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Reading data
data = pd.read_csv("datasetp3.csv") #<----Please mention file path in quotes here if Spyder IDE is not used
x= data.age
y= data.charges
X= np.column_stack([x, y])


#Linear Least squares Implementation
A = np.column_stack([x, np.ones(len(x))]) #Matrix X
Y = np.row_stack(y) #Matrix Y
E = np.matmul(A.T, A) 
F= np.linalg.inv(E)
G = np.matmul(F, A.T)
B = np.matmul(G, Y) #This is basically B = (((X^T*X)^-1) * X^T) * Y

#Calculating line equation
line =  np.matmul(A,B)
print('The values of m and c respectively:')
print(B)

plt.scatter(x,y) #Data plot
plt.plot(x, line, 'b-') #Linear Least Square fit
plt.show


