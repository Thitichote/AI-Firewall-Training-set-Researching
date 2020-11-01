import matplotlib.pyplot as plt 
  
# line 1 points 
x1 = [20,60,120,240,480,960,1920] 
y1 = [0.7645,2.6921,2.3685,3.7796,4.9719,9.3617,17.5113]
# plotting the line 1 points  
plt.plot(x1, y1, label = "Value") 


# naming the x axis 
plt.xlabel('x - Number of packets used in model (Packet)') 
# naming the y axis 
plt.ylabel('y - Trained time used')

# giving a title to my graph 
plt.title('Number of packet & Predict time') 

# show a legend on the plot 
plt.legend() 

plt.savefig('packets and model time.png')
 
# function to show the plot 
plt.show() 
