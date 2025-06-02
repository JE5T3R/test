from tkinter import *

root = Tk()

root.title("exersite 1")
root.geometry("400x400")
root.configure(bg="#879e82")

x = Label(root, text = "Hello, world!", 
          #bg is font highlight color, fg is font color, font is font style, size and thickness
          bg = "black", fg = "yellow",
          font = 'Arial 300 bold')
#x pac() is needed
x.pack()
root.mainloop()