import matplotlib.pyplot as plt 
  
# line 1 points 
x1 = [20,60,120,240,480,960,1920] 
y1 = [0.7835,0.7325,0.7345,0.8034,0.765,0.7887,0.7625]
# plotting the line 1 points  
plt.plot(x1, y1, label = "Value")


# naming the x axis 
plt.xlabel('x - Number of packets used in model (Packet)') 
# naming the y axis 
plt.ylabel('y - Predicted time used') 

# giving a title to my graph 
plt.title('Number of packets & Predict time') 

# show a legend on the plot 
plt.legend() 

plt.savefig('packets and predict time.png')  

# function to show the plot 
plt.show() 
