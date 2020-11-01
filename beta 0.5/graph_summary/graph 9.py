
import matplotlib.pyplot as plt 
  
# line 1 points 
x1 = [60,120,240,480,960,1920] 
y1 = [8.46,50.62,100,94.35,100,91.85] 
# plotting the line 1 points  
plt.plot(x1, y1, label = "TP Accuracy of N packet (r1n=r2n)") 
  
# line 2 points 
x2 = [60,120,240,480,960,1920]
y2 = [91.74,88.96,88.96,98.51,88.96,88.96] 
# plotting the line 2 points  
plt.plot(x2, y2, label = "TP Accuracy of Ratio (254:4094:254)") 
  
# naming the x axis 
plt.xlabel('x - Number of packets used in model (Packet)') 
# naming the y axis
plt.ylabel('y - True Positive Accuracy (%)') 

# giving a title to my graph 
plt.title('True Positive Accuracy with 3 Rule') 
  
# show a legend on the plot 
plt.legend()

plt.savefig('TP with 3rules.png') 
 
# function to show the plot 
plt.show() 
