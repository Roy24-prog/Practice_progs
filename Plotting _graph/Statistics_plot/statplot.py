import matplotlib.pyplot as plt
import math as m
import statistics as stats
from scipy.stats import norm
import random

x = []
y = []
z = []
n = 100

for i in range (n):
    x.append(random.randint(0, 100))
    y.append(i+1)
    
mean = stats.mean(x)
sd = stats.stdev(x) 
median = stats.median(x)

print ("Sample: ", x)
print ("Mean: ", mean)
print ("Standard Deviation: ", sd)
print ("Median: ", median)
input ("Press over...")

x.sort()
print ("Sorted sample: ", x)
input ("Press over...")



print (norm.pdf(x, mean, sd))
print (norm.cdf(x, mean, sd))

# plotting the graph
plt.plot(x, norm.pdf(x, mean, sd))
# naming the x - axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')
# giving a title to my graph
plt.title('Normal distribution - Probable density')
plt.show()

# plotting the graph
plt.plot(x, norm.cdf(x, mean, sd))
# naming the x - axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')
# giving a title to my graph
plt.title('Normal distribution - Cummulative density')
plt.show()

