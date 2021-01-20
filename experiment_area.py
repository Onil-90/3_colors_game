# Here I can experiment with new code
# before changing the other files

import numpy as np 
import random as rnd

import functions as fn


#  New
def create_pool(n, row_elem, column_elem, check_board, board):
	col = board[row_elem, check_board[row_elem, :]]
	row = board[check_board[:, column_elem], column_elem]
	pool = [x for x in range(n) if (x not in col and x not in row)]
	return pool


# Fill the upper left triangle
def fill(n):
	new_board = np.zeros([n, n]).astype(int)
	# Initialize the matrix check_board to keep
	# track of the entries that have been added
	check_board = np.zeros([n, n]).astype(bool)
	for r in range(n):
		for c in range(n):
			pool = create_pool(n, r, c, check_board, new_board)
			if pool == []:    # If there is nothing to choose it means that we made a mistake on an earlier step
				break
			elem = rnd.choice(pool)
			new_board[r,c] = elem
			check_board[r, c] = True

	return new_board

n = 5
board = np.zeros([n,n]).astype(int)
while fn.check(board) == False:
	board = fill(5)


print(board)

# Now we have to solve the rest of the square

def score(n, row_elem, column_elem, check_board):
	col = sum(check_board[row_elem,:])
	row = sum(check_board[:,column_elem])
	return max(col, row)


