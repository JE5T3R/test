import tkinter as tk
import random

def roll_dice():
    global roll_count
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
#--------------------------------------------------
#--------------------------------------------------
#--------------------------------------------------
#--------------------------------------------------
#links the labels to show the die rolls #----------
    label_die1.config(text=str(die1))   #----------
    label_die2.config(text=str(die2))   #----------
#--------------------------------------------------
#--------------------------------------------------
#--------------------------------------------------
#--------------------------------------------------

    
    roll_count += 1
    label_roll_count.config(text=f"roll count = {roll_count}")
    
    #  background to green if both dice are 6
    if die1 == 6 and die2 == 6:
        root.config(bg="green")
    else:
        root.config(bg="SystemButtonFace")
def quit_app():
    root.destroy()

root = tk.Tk()
root.title("Dice Roll")

# Roll count variable
roll_count = 0

btn_quit = tk.Button(root, text="Quit", command=quit_app, width=10)
btn_quit.grid(row=0, column=0, padx=10, pady=10)

btn_random = tk.Button(root, text="Random", command=roll_dice, width=10)
btn_random.grid(row=0, column=1, padx=10, pady=10)

label_die1 = tk.Label(root, text="0", bg="orange", width=10, height=2, font=("Arial", 16))
label_die1.grid(row=1, column=0, padx=10, pady=10)

label_die2 = tk.Label(root, text="0", bg="red", width=10, height=2, font=("Arial", 16))
label_die2.grid(row=1, column=1, padx=10, pady=10)

label_roll_count = tk.Label(root, text="roll count = 0", fg="black", font=("Arial", 12))
label_roll_count.grid(row=2, column=0, columnspan=2, pady=10)


root.mainloop()
