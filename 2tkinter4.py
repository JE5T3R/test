'''import tkinter as tk
import random

def rand ():
    global roll
    roll = random.randint(1,10)
    test.config(text=str(roll))

def quit_app():
    root.destroy()

def check():
    gess = geuss
    if gess == roll:
        message_label.config(text="Correct", bg="lime")

    else:
        root.config(bg="SystemButtonFace")


root = tk.Tk()
root.title("Random number")

btn_random = tk.Button(root, text="Random", command=rand, width=10)
btn_random.grid(row=0, column=0)

btn_check = tk.Button(root, text="Check", width=10)
btn_check.grid(row=0, column=1)

btn_quit = tk.Button(root, text="Quit", command=quit_app, width=10)
btn_quit.grid(row=0, column=2)

geuss = tk.Entry(root, width=10)
geuss.grid(row=1, column=0, padx=10, pady=10)

test = tk.Label(root, text="0", bg="orange", width=10, height=2, font=("Arial", 16))
test.grid(row=2, column=0, padx=10, pady=10)

message_label = tk.Label(root, text="Press Random to generate a random number between 1 and 10.",
                         bg="yellow", font=("Arial", 10))
message_label.grid(row=3, column=0, columnspan=3, padx=5, pady=10, sticky="NE")





root.mainloop()

'''

import tkinter as tk
import random

target_number = None

def generate_number():
    global target_number
    target_number = random.randint(1, 10)
    message_label.config(text="Random number generated! Enter your guess.", bg="yellow")

def check_guess():
    global target_number
    if target_number is None:
        message_label.config(text="Press Random to generate a number first!", bg="yellow")
        return

    try:
        guess = int(entry_guess.get())
    except ValueError:
        message_label.config(text="Please enter a valid number!", bg="red")
        return

    if guess < target_number:
        message_label.config(text="Too low", bg="red")
    elif guess > target_number:
        message_label.config(text="Too high", bg="red")
    else:
        message_label.config(text="Correct", bg="lime")

def quit_app():
    root.destroy()

root = tk.Tk()
root.title("Guess the Number")

# Buttons
btn_random = tk.Button(root, text="Random", command=generate_number, width=10)
btn_random.grid(row=0, column=0, padx=5, pady=5)

btn_check = tk.Button(root, text="Check", command=check_guess, width=10)
btn_check.grid(row=0, column=1, padx=5, pady=5)

btn_quit = tk.Button(root, text="Quit", command=quit_app, width=10)
btn_quit.grid(row=0, column=2, padx=5, pady=5)

# Entry for user guess
entry_label = tk.Label(root, text="Guess the number")
entry_label.grid(row=1, column=0, columnspan=2, pady=5)

entry_guess = tk.Entry(root, width=10)
entry_guess.grid(row=1, column=2, pady=5)

# Label for messages
message_label = tk.Label(root, text="Press Random to generate a random number between 1 and 10.",
                         width=50, bg="yellow", font=("Arial", 10))
message_label.grid(row=2, column=0, columnspan=3, padx=5, pady=10)

root.mainloop()
