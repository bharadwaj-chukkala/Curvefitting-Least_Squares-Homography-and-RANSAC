#Problem 2 part 2 
import cv2
import matplotlib.pyplot as plt
import numpy as np
Video = cv2.VideoCapture("ball_video2.mp4") #<----Please mention file path in quotes here if Spyder IDE is not used

success,frame = Video.read()
x= []
y= []

count = 0

while (Video.isOpened()):
    
    if success == False:
        break
    
    gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)        
    # convert the grayscale image to binary image
    #blur = cv2.GaussianBlur(gray_image, (5, 5), cv2.BORDER_DEFAULT)
    ret, thresh = cv2.threshold(gray_image, 200, 255, cv2.THRESH_BINARY_INV)
            
    # calculate moments of binary image
    M = cv2.moments(thresh)
            
    # calculate x,y coordinate of center
    cX = int(M["m10"] / M["m00"])
    cY = -int(M["m01"] / M["m00"])
    x.append(cX)
    y.append(cY)
    success, frame = Video.read()
    print("Read and Captured", success)
    count +=1 

x2 = np.power(x,2)
X = np.column_stack([x2 , x, np.ones(len(x))])
Y = np.row_stack(y)
E = np.matmul(X.T, X)
F= np.linalg.inv(E)
G = np.matmul(F, X.T)
B = np.matmul(G, Y) #weights

print("The weights a,b,c are:")
print(B)

line =  np.matmul(X,B)

plt.scatter(x,y)
plt.plot(x, line, 'g')
plt.show()
