import numpy as np
import random as rnd

from functions import *



# Inizio gioco

exit = False
while exit == False: 
	print('\n')
	print('*** A B C GAME ***')
	print('\n')
	is_ans_valid = False
	while is_ans_valid == False:
		print('Do you want to play? (y/n)')
		ans = input()
		if (ans == 'y' or ans == 'n'):
			is_ans_valid = True
		else:
			print('\n')
			print('This is not a valid answer.')
			print('Please enter \'y\' or \'n\'!')
			print('\n')
	if ans == 'y':
		# HERE SHOULD GO THE GAME
		# 
		board = create_game(5)
		#print(board)
		a = info(board)
		print(a['n'])

		exit = False
	if ans == 'n':
		print('\n')
		print('Too bad. See you next time!')
		exit = True
	