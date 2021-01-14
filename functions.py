
import numpy as np
import random as rnd

# Function that checks whether the given board satisfies the rules or not. 
# Rules: 
# There are three carachters 'a', 'b', 'c' (repeated exactly once) per row and per column (the other 2 are empty)
# I'm going to use 1, 2, 3 instead of 'a', 'b', 'c', because it's easier. The empty slots will be 0s. 

def check(board):
	count = 0
	for r in range(board.shape[0]):
		count = count + (sum(np.sort(board[r,:]) - [0, 1, 2, 3, 4]))**2
	for c in range(board.shape[1]):
		count = count + (sum(np.sort(board[c,:]) - [0, 1, 2, 3, 4]))**2
	if count == 0:
		res = True
	else:
		res = False
	return res


#--------------------------------------------------------


# Permutation of 1, 2, 3, 4, 5

def rand_perm(n):
	a = range(n)
	per = []
	for i in range(n):
		x = rnd.choice(a)
		per.append(x)
		a.remove(x)
	return per


#-------------------------------------------------------
# This function takes an np.array and a number as input. 
# I have in mind a permutation of range(n) and a number numb in range n as input
# (IT BRAKES DOWN IN OTHER SITUATIONS!!! Maybe take care of that in a future)
#
# Returns the original array cyclically permuted in order to have numb as 
# first entry

def cyclic_perm(arr, numb):
	new_arr = np.array([])
	index = np.where(arr ==numb)[0][0]
	for i in range(5):
		new_arr = np.append(new_arr, arr[(i +index)%5])
	new_arr = new_arr.astype(int)
	return new_arr