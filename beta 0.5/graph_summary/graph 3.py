import matplotlib.pyplot as plt 
  
# line 1 points 
x1 = [20,60,120,240,480,960,1920] 
y1 = [82.11, 87.47, 90.66, 93.86, 97.02, 93.86, 95.01]
# plotting the line 1 points  
plt.plot(x1, y1, label = "Value") 


# naming the x axis 
plt.xlabel('x - Number of packets used in model (Packet)') 
# naming the y axis 
plt.ylabel('y - Accuracy (%)') 

# giving a title to my graph 
plt.title('Accuracy of model with 1 Rule') 

# show a legend on the plot 
plt.legend() 

plt.savefig('accuracy_1rule.png')  

# function to show the plot 
plt.show() 
