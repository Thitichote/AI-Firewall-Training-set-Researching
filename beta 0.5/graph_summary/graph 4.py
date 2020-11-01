
import matplotlib.pyplot as plt 
  
# line 1 points 
x1 = [20,60,120,240,480,960,1920] 
y1 = [100,100,100,100,100,100,100] 
# plotting the line 1 points  
plt.plot(x1, y1, label = "True Positive") 
  
# line 2 points 
x2 = [20,60,120,240,480,960,1920] 
y2 = [64.22,74.94,81.32,87.73,94.05,87.73,90.03] 
# plotting the line 2 points  
plt.plot(x2, y2, label = "True Negative") 
  
# naming the x axis 
plt.xlabel('x - Number of packets used in model (Packet)') 
# naming the y axis 
plt.ylabel('y - Accuracy (%)') 

# giving a title to my graph 
plt.title('Accuracy of model with 1 Rule') 
  
# show a legend on the plot 
plt.legend() 

plt.savefig('TP and NP with 1rule.png')  

# function to show the plot 
plt.show() 
