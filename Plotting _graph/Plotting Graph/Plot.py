# importing the required module
import matplotlib.pyplot as plt
import math as m
import numpy as np
import random
import pandas as pd

cf = []
y = []
ar = []
# x axis values
# n = int(input("Enter range: "))

n = 54
d = {'col1': [1,2,3,5,6,7], 'col2': [3,4,5,8,5,6]}
df = pd.DataFrame(data=d)  
print(df)
print(d)

ar = df['col2'].to_numpy()
print(ar)
length = len(ar)

for i in ar:
    sum= sum + i 
    cf.append(sum)
   
print(cf)
# print (x)
# plotting the graph    
# plt.hist(df)    #plt.what_not    
# naming the x axis
input("Press over...")
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')
# giving a title to my graph
plt.title('Bar plot')    
# function to show the plot
# plt.show()