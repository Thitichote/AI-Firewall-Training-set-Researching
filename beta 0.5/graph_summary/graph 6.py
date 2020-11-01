
import matplotlib.pyplot as plt 
  
# line 1 points 
x1 = [60,120,240,480,960,1920] 
y1 = [4.33,73.5,94.11,94.11,94.11,94.11] 
# plotting the line 1 points  
plt.plot(x1, y1, label = "TP Accuracy of N packet (r1n=r2n)") 
  
# line 2 points 
x2 = [60,120,240,480,960,1920]
y2 = [90.23,94.11,94.11,94.11,94.11,94.11] 
# plotting the line 2 points  
plt.plot(x2, y2, label = "TP Accuracy of Ratio (254:4094)") 
  
# naming the x axis 
plt.xlabel('x - Number of packets used in model (Packet)') 
# naming the y axis 
plt.ylabel('y - True Positive Accuracy (%)') 

# giving a title to my graph 
plt.title('True Positive Accuracy with 2 Rule')
  
# show a legend on the plot 
plt.legend()

plt.savefig('TP with 2rules.png')  

# function to show the plot 
plt.show() 
