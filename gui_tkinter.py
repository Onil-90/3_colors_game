from tkinter import *
import numpy as np
from functions import *






# create window called root
root = Tk()
# Assign title to window
root.title("My first GUI desktop app")
# Set  the min size
#window.minsize(500,500)
# Set the color of the background to  be black
root.configure(background="black")
# Set the margin around buttons
v_margin = 10
h_margin = 4


# Create game (i.e. solution) in numeric form
board = create_board(5)

# Get n, s, w, e info
dic_info = info(board)
north = dic_info['n']
south = dic_info['s']
east = dic_info['e']
west = dic_info['w']


# Solution matrix 
global solution_matrix
solution_matrix = -1*np.ones([5,5]).astype(int)

global array_col
global colors 
colors =  ['red', 'green', 'yellow', 'white']
global 	test_board 
test_board = board    		# I create a new board where
test_board[test_board>=3]=-1 

# Function for change color of buttons
def color_change(btn,r,c):
    ind = array_col[r,c]			
    btn.config(bg=colors[ind], activebackground = colors[ind])	# change color
    array_col[r,c] = (array_col[r,c] + 1)%4 					# update the array storing colors
    solution_matrix[r,c] = ind									# update solution matrix    
    if ind >=3:
    	solution_matrix[r,c] = -1
    print(solution_matrix)										# print sol matrix for debugging

# Function for very the solution
def verify():
	bool_matr = (solution_matrix==test_board)
	if bool_matr.all() == True:
		answer.config(text="WIN!!! :)")
	else:
		answer.config(text="Keep trying...")




# New game button
new_game = Button (root, bg='black', fg='white', text="New Game", activebackground = 'white') 
new_game.grid(row=0,column=3,  pady = v_margin, padx = h_margin)
# Exit button
exit = Button (root, bg='black', fg='white', text="Exit", activebackground = 'red') 
exit.grid(row=10,column=4, pady = v_margin, padx = h_margin)

# Submit button
submit = Button (root, bg='black', fg='white', text="Check", activebackground = 'white', command=verify) 
submit.grid(row=10,column=2, pady = v_margin, padx = h_margin)
# Answer (TEXT)
answer = Label (root, bg = 'white', fg='black', width= 10, height=2)
answer.grid(row=10, column= 3)




#---------------- INFO NORTH
for i in range(5):
	Label (root, bg=colors[north[i]], width=10, height = 2).grid(row=1, column=i+1)
#---------------- INFO SOUTH
for i in range(5):
	Label (root, bg=colors[south[i]], width=10, height = 2).grid(row=7, column=i+1)
#---------------- INFO WEST
for i in range(5):
	Label (root, bg=colors[west[i]], width=5, height = 4).grid(row=i+2, column=0)
#---------------- INFO EAST
for i in range(5):
	Label (root, bg=colors[east[i]], width=5, height = 4).grid(row=i+2, column=6)

# --- main ---

array_col = np.zeros([5,5]).astype(int)
array_col[0,0]=1


for r in range(5):
	for c in range(5):
		btn = Button(text=" ", width=10, height=5)
		btn.grid(row=r+2, column=c+1)
		btn['command'] = lambda btn=btn,r=r, c=c: color_change(btn,r,c) # Assign a command


root.mainloop()

