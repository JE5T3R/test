from tkinter import *

def click():
    global count
    count += 1
    label_text.set(count)

root = Tk()
root.title("exercise 3")

count = 0
label_text = IntVar()
label_text.set(0)

label_1 = Label(root, font = "Arial 40 bold", textvariable=label_text)
label_1.pack()

button_1 = Button(root, text = "Click me", bg = "black", fg = "yellow", font = ("Arial 35 bold"), command = click)

button_1.pack(fill=X)


root.mainloop()