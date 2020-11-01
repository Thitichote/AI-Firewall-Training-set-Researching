
import matplotlib.pyplot as plt 
  
# line 1 points 
x1 = [60,120,240,480,960,1920] 
y1 = [85.08,75.03,61.3,79.62,63.54,83.8] 
# plotting the line 1 points  
plt.plot(x1, y1, label = "TN Accuracy of N packet (r1n=r2n)") 
  
# line 2 points 
x2 = [60,120,240,480,960,1920]
y2 = [63.69,73.92,78.65,68.19,83.08,89.49] 
# plotting the line 2 points  
plt.plot(x2, y2, label = "TN Accuracy of Ratio (254:4094:254)") 
  
# naming the x axis 
plt.xlabel('x - Number of packets used in model (Packet)') 
# naming the y axis
plt.ylabel('y - True Negative Accuracy (%)') 

# giving a title to my graph 
plt.title('True Negative Accuracy with 3 Rule') 
  
# show a legend on the plot 
plt.legend()

plt.savefig('NP with 3rules.png')  
# function to show the plot 

plt.show() 
