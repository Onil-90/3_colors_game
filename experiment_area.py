# Here I can experiment with new code
# before changing the other files

import numpy as np 
import functions as fn

board = np.array([[3, 4, 1, 0, 2],
		 		 [4, 0, 2, 3, 1],
		 		 [2, 3, 0, 1, 4],
		 		 [1, 2, 3, 4, 0],
		 		 [0, 1, 4, 2, 3]])

print(board)

perm = fn.rand_perm(5)
a = np.array(perm)
print(perm)

n = 3
print(n)
print("the index of ")
print(n)
print("is ")
index = np.where(a==n)[0][0]
print(index)

c = np.array([])

for i in range(5):
	c = np.append(c, a[(i+index)%5])

c = c.astype(int)

print(c)

# Trasform the mess above in a function

def cyclic_perm(arr, numb):
	new_arr = np.array([])
	index = np.where(arr ==numb)[0][0]
	for i in range(5):
		new_arr = np.append(new_arr, arr[(i +index)%5])
	new_arr = new_arr.astype(int)
	return new_arr

print(cyclic_perm(a, 3))