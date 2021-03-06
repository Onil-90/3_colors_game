from tkinter import *
from functions import *


# key down function
def click():
	entered_text=textentry.get() # this will collect the text from the textentry box
	output.delete(0.0, END)
	try:
		answer = my_dictionary[entered_text]
	except:
		answer = "Sorry my friend. This is not a valid answer. Try again."
	output.insert(END, answer)	

# Exit function
def close_window():
	window.destroy() # destroy window
	exit() # exit the programdata scientist





# Create window
window = Tk()
# Assign title to window
window.title("My first GUI desktop app")
# Set  the min size
#window.minsize(500,500)
# Set the color of the background to  be black
window.configure(background="black")

#------------------------------------

# Create a text (bg is the background color of the text, fg is the foreground color)
Label (window, text="Welcome to the ABC game", bg="black", fg="white", font ="none 12 bold").grid(row=0, column=0, sticky=W)

# --------------------------------------

## Create a text entry
#textentry = Entry(window, width=20, bg="white")
#textentry.grid(row=1, column=0, sticky=W)

#---------------------------------------

# Create a button
for r in range(5):
	for c in range(5):
		Button (window, text=" ", width=6, height=3, command=click) .grid(row=r+1, column=c+1, sticky=W)



window.mainloop()


