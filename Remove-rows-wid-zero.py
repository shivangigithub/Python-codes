##remove row with zeros, (numpy)
import numpy as np
# take data
# data = np.array([[1, 2, 0], [0, 0, 0], [4, 5, 6],
                 # [0, 0, 0], [7, 8, 9], [0, 0, 0]])
# print original data having rows with all zeroes
data = np.loadtxt("int.txt", dtype=int) #import data as integer
print("Original Dataset")
print(data)
 
# remove rows having all zeroes
data = data[~np.all(data == 0, axis=1)] #if axis =0, that means if column[i] contains all zeros, then it will remove row[i]
#if axis =1, that means if row[i] contains all zeros, then it will remove row[i]# data after removing rows having all zeroes
print("After removing rows")
print(data)