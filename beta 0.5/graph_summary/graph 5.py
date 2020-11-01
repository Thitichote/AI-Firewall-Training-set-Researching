
import matplotlib.pyplot as plt 
  
# line 1 points 
x1 = [60,120,240,480,960,1920] 
y1 = [50.33,78.66,79.15,87.42,91.77,92.17] 
# plotting the line 1 points  
plt.plot(x1, y1, label = "Accuracy of N packet (r1n=r2n)") 
  
# line 2 points 
x2 = [60,120,240,480,960,1920]
y2 = [64.58,85.04,88.26,85.12,87.88,87.85] 
# plotting the line 2 points  
plt.plot(x2, y2, label = "Accuracy of Ratio (254:4094)") 
  
# naming the x axis 
plt.xlabel('x - Number of packets used in model (Packet)') 
# naming the y axis 
plt.ylabel('y - Accuracy (%)') 

# giving a title to my graph 
plt.title('Accuracy of model with 2 Rule') 
  
# show a legend on the plot 
plt.legend() 

plt.savefig('accuracy_2rules.png')  

# function to show the plot 
plt.show() 
