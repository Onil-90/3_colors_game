**What is this thing**

In the Italian puzzle magazine *La Settimana Enigmistica* (https://en.wikipedia.org/wiki/La_Settimana_Enigmistica) there is a simple Sudoku-like puzzle called **ABBICI'**. This is a python implementation of that game.
The magazine version of the puzzle is with letters (**A**,**B**, **C**) instead of colors.

This repo consists of two files: 
- **functions.py** is the backbone of the project
- **gui_tkinter.py** is the interface to actually play the game (it's my very first GUI!).


**How to play the game**

When you run the GUI you will see a 5x5 matrix of buttons surrounded by colors. If you click on a button it will change color.
You have to fill the matrix in such a way that each row and column will contain exactly one of the 3 colors **red**, **yellow**, **green**. Therefore each row and column will have two empty (**white**) spots. 
The colors on the rim of the matrix tell you what color (inside the matrix) is the closest to the rim in that particular row or column.

You can check whether your solution is correct by clicking the button **Check**. 

