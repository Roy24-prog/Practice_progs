# importing the required module
import matplotlib.pyplot as plt
import math as m
import numpy as np
import statistics
import pandas as pd

cf = []
y = []
ar = []
sum = 0
array = []
# x axis values
# n = int(input("Enter range: "))

d = {'__Range': [1,2,3,4,5,6,7,8,9,10], '__Freq': [81, 95, 92, 92, 100, 115, 117, 111, 98, 96]}
df = pd.DataFrame(data=d)

print(df)

ar = df['__Freq'].to_numpy()

for i in ar:
    sum= sum + i 
    cf.append(int(sum))

d['__CF'] = cf
df = pd.DataFrame(data=d)
print(df)
x=df['__Range'].to_numpy()
y=df['__Freq'].to_numpy()
z=df['__CF'].to_numpy()

# input("Press over...")

sd = statistics.stdev(df['__Freq'])
median = statistics.median(df['__Freq'])

print("Standard deviation: ", sd)
print("Median: ", median)
print(df.info())
print(df.describe())
# print (x)
# plotting the graph    
plt.plot(x, z)    #plt.what_not    
# naming the x axis

plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')
# giving a title to my graph
plt.title('Plot')    
# function to show the plot
plt.show()