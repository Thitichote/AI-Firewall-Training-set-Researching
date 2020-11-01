
import matplotlib.pyplot as plt 
  
# line 1 points 
x1 = [60,120,240,480,960,1920] 
y1 = [46.77,62.824,80.65,86.98,81.77,87.25] 
# plotting the line 1 points  
plt.plot(x1, y1, label = "Accuracy of N packet (r1n=r2n)") 
  
# line 2 points 
x2 = [60,120,240,480,960,1920]
y2 = [77.715,81.44,83.80,83.35,86.02,89.25] 
# plotting the line 2 points  
plt.plot(x2, y2, label = "Accuracy of Ratio (254:4094:254)") 
  
# naming the x axis 
plt.xlabel('x - Number of packets used in model (Packet)') 
# naming the y axis
plt.ylabel('y - Accuracy (%)') 

# giving a title to my graph 
plt.title('Accuracy of model with 3 Rule') 
  
# show a legend on the plot 
plt.legend()

plt.savefig('accuracy_3rules.png')

# function to show the plot 
plt.show() 
