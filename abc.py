import numpy as np
import random as rnd

from functions import check

# Create board

board_0 = np.zeros((5,5))

board = np.array([[3, 4, 1, 0, 2],
		 		 [4, 0, 2, 3, 1],
		 		 [2, 3, 0, 1, 4],
		 		 [1, 2, 3, 4, 0],
		 		 [0, 1, 4, 2, 3]])
print(board)

board_1 = np.array([[2, 4, 0, 3, 1],
		 		    [0, 1, 4, 2, 3],
		 		    [4, 0, 3, 1, 2],
		 		    [1, 3, 2, 4, 0],
		 		    [3, 2, 1, 0, 4]])
print(board_1)




#--------------------------------------------------------

print check(board)
print check(board_1)

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

#------------------------------------------------------
print rand_perm(5)
#------------------------------------------------------

#print np.linalg.det(board)  # Compute determinant
#print np.linalg.det(board_1)

# Da fare: 
# 
# - Scrivere funzione che permuti righe e colonne (def perm(board, r_or_c, (i,j)) and return the new board )
# - Scrivere funzione che legge una board e restituisce la matrice vuota con le informazioni lungo il bordo.
# - Scrivere il programma vero e proprio, che seleziona un insieme di permutazioni casuale e crea il nuovo board e crea la partita.



#======================================================================================

# Function for creating game

# def game(board): 
# 	l = len(board)
# 	game_board = np.zeros((l+2, l+2))
# 	game_board[1:(l+1), 1:(l+1)] = board

# 	for i in range(5):
# 		vec = board[:,i]
# 		vec = list(vec)
# 		vec = vec.remove(0)
# 		vec = vec.remove(0)
# 		game_board[0, i +1] = vec[0]
# 		game_board[l+2, i + 1] = vec[2]

# 	return game_board

# print(game(board)) # for debugging


