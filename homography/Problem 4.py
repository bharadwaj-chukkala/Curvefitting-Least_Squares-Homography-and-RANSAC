import numpy as np

x1, x2, x3, x4 = 5,150,150,5
y1, y2, y3, y4 = 5,5,150,150
xp1, xp2, xp3, xp4 = 100, 200, 220, 100
yp1, yp2, yp3, yp4 = 100, 80, 80, 200

A =np.array( [[-x1,-y1,-1,0,0,0,x1*xp1,y1*xp1,xp1],
             [0,0,0,-x1,-y1,-1,x1*yp1,y1*yp1,yp1],
             [-x2,-y2,-1,0,0,0,x2*xp2,y2*xp2,xp2],
             [0,0,0,-x2,-y2,-1,x2*yp2,y2*yp2,yp2],
             [-x3,-y3,-1,0,0,0,x3*xp3,y3*xp3,xp3],
             [0,0,0,-x3,-y3,-1,x3*yp3,y3*yp3,yp3],
             [-x4,-y4,-1,0,0,0,x4*xp4,y4*xp4,xp4],
             [0,0,0,-x4,-y4,-1,x4*yp4,y4*yp4,yp4]]) 

print("The A Matrix is")
print(A)

def calc_SVD(A):
    AT= A.T
    AAT= A.dot(AT)
    ATA= AT.dot(A)
    eigval_U, eigvec_U = np.linalg.eig(AAT)
    eigval_V, eigvec_V = np.linalg.eig(ATA)
    sort_eigval_U =  eigval_U.argsort()[::-1] #sorted eigenvalues of eigval_U
    sort_eigval_V =  eigval_V.argsort()[::-1] #sorted eigenvalues of eigval_V
    U = eigvec_U[:, sort_eigval_U]
    V = eigvec_V[:, sort_eigval_V]
    VT = V.T
    sigma =  np.sqrt(eigval_U)
    E = np.diag(sigma)
    H = VT[:,8]
    H = np.reshape(H,(3,3))
    return VT, U, E, H


#Return decomposed values of A
VT, U, E, H = calc_SVD(A)

np.set_printoptions(suppress = True)
print("V Transpose =") 
print (VT)
print("U=") 
print (U)
print("Sigma=") 
print(E)
print("Homography Matrix=")
print(H)

   
#print(eigval_U)
#print(eigvec_U)
