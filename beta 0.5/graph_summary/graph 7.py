
import matplotlib.pyplot as plt 
  
# line 1 points 
x1 = [60,120,240,480,960,1920] 
y1 = [96.34,83.83,58.31,74.85,89.44,90.25] 
# plotting the line 1 points  
plt.plot(x1, y1, label = "TN Accuracy of N packet (r1n=r2n)") 
  
# line 2 points 
x2 = [60,120,240,480,960,1920]
y2 = [38.94,75.97,82.41,76.14,81.66,81.60] 
# plotting the line 2 points  
plt.plot(x2, y2, label = "TN Accuracy of Ratio (254:4094)") 
  
# naming the x axis 
plt.xlabel('x - Number of packets used in model (Packet)') 
# naming the y axis
plt.ylabel('y - True Negative Accuracy (%)') 

# giving a title to my graph 
plt.title('True Negative Accuracy with 2 Rule') 
  
# show a legend on the plot 
plt.legend()

plt.savefig('NP with 2rules.png')  
# function to show the plot 
plt.show() 
