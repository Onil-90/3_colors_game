# Here I can experiment with new code
# before changing the other files

import numpy as np 
import random as rnd

import functions as fn

board = np.array([[3, 4, 1, 0, 2],
		 		 [4, 0, 2, 3, 1],
		 		 [2, 3, 0, 1, 4],
		 		 [1, 2, 3, 4, 0],
		 		 [0, 1, 4, 2, 3]])

print(board)

perm = fn.rand_perm(5)
a = np.array(perm)
a = a.astype(int)
print(perm)


# Trasform the mess above in a function

def cyclic_perm(arr, numb):
	new_arr = np.array([])
	index = np.where(arr ==numb)[0][0]
	for i in range(5):
		new_arr = np.append(new_arr, arr[(i +index)%5])
	new_arr = new_arr.astype(int)
	return new_arr

#--------------------------------------

new_board = np.zeros([5, 5]).astype(int)

for col in range(5):
	arr = board[:, col]
	asd = cyclic_perm(arr, a[col])
	for row in range(5):
			new_board[row, col] = asd[row]

print(new_board)


# Minchia.... non sembra funzionare


#---------------------------------
# Provo un altro approccio. Invece che 
# partire gia da una matrice, la creo da zero


n = 5

new_board = np.zeros([n, n]).astype(int)
# first row totally random
new_board[0,:] = fn.rand_perm(n)
print(new_board)
# secon row 
# create a list with the elements
list_num = range(n)
for c in range(n):
	elem_up = new_board[0,c]
	was_elem_up_removed = 0
	if elem_up in list_num:
		list_num.remove(elem_up) # I remove from the pool the element in the same column 
		was_elem_up_removed = 1
	new_el = rnd.choice(list_num)
	print(new_el)
	new_board[1,c] = new_el
	if was_elem_up_removed == 1:
		list_num.append(elem_up) # We put the number above in the column back in the pool
	if new_el in list_num:
		list_num.remove(new_el) # We don't want repetitions on the row
	

# FUNZIONA ECCETTO NEL CASO IN CUI L'ULTIMO ELEMENTO DELLA 
# SECONDA RIGA E' FORZATO AD ESSERE UGUALE A QUELLO DELLA PRIMA

# To do: risolvere il bug! Idea: fermarsi uno step prima e controllare gli ultimi due numeri 
# Trovare un modo (ricorsivo?) per fare le altre righe

print(new_board)

# ALTRA IDEA: riempire la matrice un elemento alla volta provando casualmente ogni numero in 
# range(n) finche uno non va bene. Scrivere una funzione di check.. magari tenere traccia 
# degli elementi già modificati con una matrice di 0 e 1

