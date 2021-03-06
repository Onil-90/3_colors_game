
import numpy as np
import random as rnd

# Function that checks whether the given board satisfies the rules or not. 
# Rules: 
# There are three carachters 'a', 'b', 'c' (repeated exactly once) per row and per column (the other 2 are empty)
# I'm going to use 1, 2, 3 instead of 'a', 'b', 'c', because it's easier. The empty slots will be 0s. 

def check(board):
	count = 0
	for r in range(board.shape[0]):
		count = count + (sum(np.sort(board[r,:]) - range(board.shape[0])))**2
	for c in range(board.shape[1]):
		count = count + (sum(np.sort(board[c,:]) - range(board.shape[1])))**2
	if count == 0:
		res = True
	else:
		res = False
	return res



#-------------------------------------------------------
#
# The function create_pool(...) creates the pool of element from which 
# I can draw randomly to create the board. The element board[r,c]
# is selected randomly from the elements in range(n) which have not 
# been already used in the same row and column. 
# The matrix check_board keeps track of which entries of board have been
# filled already and which entries are still empty.

def create_pool(n, row_elem, column_elem, check_board, board):
	col = board[row_elem, check_board[row_elem, :]]
	row = board[check_board[:, column_elem], column_elem]
	pool = [x for x in range(n) if (x not in col and x not in row)]
	return pool


# The function fill(...) creates a board. However it is not perfect. 
# It iterates over all the entries of the board and it fills randomly from
# the pool created using create_pool(...). 
# It doesn't always work because
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


# Create board
def create_board(n):
	board = np.zeros([n,n]).astype(int)
	while check(board) == False:
		board = fill(n)
	return board

# Create game 
def create_game(n):
	board = create_board(n)
	for r in range(n):
		for c in range(n):
			if board[r,c] == 0:
				print(' a ', end = '')
			if board[r,c] == 1:
				print(' b ', end = '')
			if board[r,c] == 2:
				print(' c ', end = '')
			if board[r,c] >= 3:
				print(' * ', end = '')
			if c==(n-1):
				print('\n')
	return board


# Create info arrays (takes numerical matrix in input)
def info(board):
	n = np.shape(board)[0]
	north = np.array(range(n)).astype(int)
	south = np.array(range(n)).astype(int)
	west = np.array(range(n)).astype(int)
	east = np.array(range(n)).astype(int)

	for c in range(n):
		column = board[:,c]
		# discard 4 and 5
		e = column[column<=2]
		north[c] = e[0]
		south[c] = e[-1]

	for r in range(n):
		row = board[r,:]
		# discard 4 and 5
		e = row[row<=2]
		west[r] = e[0]
		east[r] = e[-1]

	print("north: ", north)
	print("south: ", south)
	print("west: ", west)
	print("east: ", east)
	dic = {'n':north, 's':south, 'e':east, 'w':west}
	return dic