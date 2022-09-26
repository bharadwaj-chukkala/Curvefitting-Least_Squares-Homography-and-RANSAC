#RANSAC
import random
import math
import matplotlib.pyplot as plt
import pandas as pd

#Reading the data
data = pd.read_csv("datasetp3.csv") #<----Please mention file path in quotes here if Spyder IDE is not used

x= data.age 
y= data.charges

#Fucntion for selecting two random points from the sample
def randpts(i, data):
    x1, y1 = random.choice(list(zip(x,y)))
    x2, y2 = random.choice(list(zip(x,y)))
    
    try:
        m = (y2-y1)/(x2-x1) #slope of line
    except:
        m = 0
        return 0, 0, 0
    
    C = y1 - (m*x1)
    #xpts = [x1,x2]
    #ypts = [C -(m*x) for x in xpts]
    
    #Now we have to find the perpendicular distance between line and point 
    # ax+by+c/(a^2 + b^2)^0.5
    
    a = -m #slope
    b = 1  
    c = -C #Y-intercept
    
    #Defining a threshold to separate inliers and outliers  
    Thresh = 2
    
    inlier_count = 0
    x_inliers = []
    y_inliers = []
    for d in list(zip(x,y)):
        i = d[0]
        j= d[1]
        dist = abs(a*i + b*j + c)/math.sqrt(a**2 + b**2)
        if dist < Thresh:
            x_inliers.append(x)
            y_inliers.append(y)
            inlier_count += 1   
            
    return m, C, inlier_count


#Calling the Functions 
if __name__ == "__main__":
    
    fin_inlier_count = 0
    fin_m = []
    fin_c = []

    for i in range(100):
        
        m, C, inlier_count = randpts(i, data)

        if inlier_count > fin_inlier_count:
            fin_inlier_count = inlier_count #Most number of inliers possible for the given threshold value
            fin_m = m #final slope
            fin_c = C #final intercept
        
   
    plt.scatter(x,y)
    xmin = min(x)
    xmax = max(x)
    
    ymin = fin_m*xmin + fin_c
    ymax = fin_m*xmax + fin_c
    
    plt.plot([xmin, xmax], [ymin, ymax], 'r-')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    