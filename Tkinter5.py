from tkinter import *

def quit():
    root.destroy()

def print_text():
    print(box.get())

root = Tk()
root.title("Exersie 5")
root.resizable(0,0)

entry1 = Entry(root, width=30)
entry1.pack()

sign = Label(root, width=30, text="+")
sign.pack()

entry2 = Entry(root, width=30)
entry2.pack()

box = Entry(root, justify=CENTER)
box.pack(fill = X, ipady=10)



button_print = Button(root, text = "print", width = 10, command=print_text )
button_print.pack(side = LEFT, ipady=10, padx=10, pady=10)

button_quit = Button(root, text="Quite", width=10, command=quit)
button_quit.pack(side = LEFT, ipady=10, padx=10, pady=10)

root.mainloop()