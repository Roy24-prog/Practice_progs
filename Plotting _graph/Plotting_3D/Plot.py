# importing the required module
import matplotlib.pyplot as plt
import math as m
import numpy as np
import random


x = []
y = []

# x axis values
# n = int(input("Enter range: "))

n = 54

for i in range(n):
    x.append(random.randint(15, 100))
    
print (x)
# plotting the graph    
plt.hist(x)        
# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')
# giving a title to my graph
plt.title('Bar plot')    
# function to show the plot
plt.show()