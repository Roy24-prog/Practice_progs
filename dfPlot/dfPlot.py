import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

d =  {}
columns = ['Col_1_22C', 'Col_1_27C', 'pif4-101_22C', 'pif4-101_27C', 'pif5-1_22C', 'pif5-1_27C', 'pif7-2_22C', 'pif7-2_27C', 'PIF4-OE_22C', 'PIF4-OE_27C']

d['22_degree_C'] = pd.DataFrame(columns=['Col_1_22C', 'pif4-101_22C', 'pif5_22C', 'pif7-2', 'PIF4-OE'],
                                 data=[[0.11,0.083,0.093,0.091,0.284],
                                       [0.116,0.098,0.097,0.088,0.276],
                                       [0.111,0.138,0.095,0.088,0.252],
                                       [0.101,0.063,0.095,0.123,0.259],
                                       [0.149,0.088,0.098,0.103,0.277],
                                       [0.13,0.116,0.074,0.151,0.287],
                                       [0.104,0.081,0.11,0.105,0.27],
                                       [0.106,0.081,0.084,0.072,0.285],
                                       [0.107,0.081,0.094,0.094,0.275],
                                       [0.141,0.099,0.096,0.087,0.256]])

d['27_degree_C'] = pd.DataFrame(columns=['Col_1', 'pif4-101', 'pif5-1', 'pif7-2', 'PIF4-OE'],
                                 data=[[0.21,0.144,0.198,0.204,0.381],
                                       [0.254,0.114,0.23,0.212,0.433],
                                       [0.234,0.1,0.189,0.21,0.454],
                                       [0.202,0.105,0.171,0.241,0.403],
                                       [0.277,0.091,0.198,0.201,0.536],
                                       [0.2,0.121,0.207,0.195,0.457],
                                       [0.174,0.102,0.2,0.205,0.426],
                                       [0.166,0.083,0.199,0.176,0.359],
                                       [0.188,0.11,0.183,0.177,0.46],
                                       [0.23,0.097,0.205,0.235,0.45]])

print ("Dictionary: ")

for i in d:
    print (d[i])
    # print (d[i].describe())

print("Dictionary dataframes: ", *d)

# print (len(d))
new_list = []
cluster = []
mean_set = []

for i in d:
    for j in d[i]:
         new_list.append(d[i][j].tolist())

print("List data >>>")
print (new_list)

for x in range(0,5):
    cluster.append(new_list[x])
    cluster.append(new_list[x+5])
    
for count in range (len(cluster)):
    mean_set.append(float(np.mean(cluster[count])))

print("=================") 
print ("Mean set: ",mean_set)
print("=================") 

plt.bar(columns, mean_set)
plt.ylabel("Mean values")
plt.show()


