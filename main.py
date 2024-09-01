from tkinter import *
import random

main = Tk()
main.title("Number Guessing Game")
main.geometry("700x700")
font = ('Times', 30, 'bold')
font1 = ('Times', 15, 'bold')

# Title
tt = Label(main, text="NUMBER GUESSING GAME")
tt.config(font=font)
tt.place(x=100, y=50)

# Input Label
l1 = Label(main, text="Enter your number: ")
l1.config(font=font1)
l1.place(x=50, y=150)

# Input Field
n = IntVar()
e1 = Entry(main, textvariable=n)
e1.config(font=font1)
e1.place(x=250, y=150)

# Random number generation (outside the function)
number = random.randint(1, 100)

# Feedback Label (to show if the guess is too high, too low, or correct)
feedback = Label(main, text="")
feedback.config(font=font1)
feedback.place(x=200, y=200)

# Guessing function
def guessing():
    guess = n.get()  # Get the user's guess
    if guess < number:
        feedback.config(text="Guess Higher")
    elif guess > number:
        feedback.config(text="Guess Lower")
    else:
        feedback.config(text="You Won..!")

# Button
b1 = Button(main, text="Guess", command=guessing)
b1.config(font=font1)
b1.place(x=301, y=350)

b2=Button(main,text="Exit",command=main.quit)
b2.config(font=font1)
b2.place(x=305,y=450)

main.mainloop()
