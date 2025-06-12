'''
In this first version of MY code the main idea is getting the program sorted and all the basic functions sorted such as the buttons to change the temperture calculator


from tkinter import *

root = Tk()
root.title("Temperature Converter")
root.geometry("400x400")
root.resizable(0,0)

style = "Arial 15"

def quit_program():
    print("Goodbye world")
    root.destroy()

def tocent():
    root = Tk()
    root.title("Converting to Centigrade")
    title_frame = Label(root, text = "Enter temperature in Fahrenheit", font = ("Arial", "21", "bold"))
    title_frame.grid(row = 0, column = 0, columnspan = 2)
    title_frametocent = Entry(root)
    title_frametocent.grid(row=1, column=0)

def tofah():
    root = Tk()
    root.title("Converting to Fahrenheit")
    title_frame = Label(root, text = "Enter temperature in Cenigrade", font = ("Arial", "21", "bold"))
    title_frame.grid(row = 0, column = 0, columnspan = 2)
    title_frametofah = Entry(root)
    title_frametofah.grid(row=1, column=0)


#Main program
title_frame = Label(root, text = "Temperature Converter", font = ("Arial", "21", "bold"))
title_frame.grid(row = 0, column = 0, columnspan = 2)

left_frame = Button(root, text = "to Centigrade", bg = "yellow", font = style, command = tocent)
left_frame.grid(row = 1, column = 0)

right_frame = Button(root, text = "to Fahrenheit", bg = "red", font = style, command = tofah)
right_frame.grid(row = 1, column = 1)

root.mainloop()'''

from tkinter import *

root = Tk()
root.title("Temperature Converter")
root.geometry("400x200")
root.resizable(0, 0)

style = "Arial 15"

# Function to raise a frame
def show_frame(frame):
    frame.tkraise()

def quit_program():
    print("Goodbye world")
    root.destroy()

# -------- Main container frame ----------
container = Frame(root)
container.pack(fill="both", expand=True)

# --------- Frame 1: Main Menu ----------
frame_main = Frame(container)
frame_main.place(relwidth=1, relheight=1)

title_label = Label(frame_main, text="Temperature Converter", font=("Arial", 21, "bold"))
title_label.pack(pady=10)

# Button row (L and R side-by-side)
button_frame = Frame(frame_main)
button_frame.pack()

btn_cent = Button(button_frame, text="to Centigrade", bg="yellow", font=style, command=lambda: show_frame(frame_cent))
btn_cent.pack(side=LEFT, padx=10)

btn_fahr = Button(button_frame, text="to Fahrenheit", bg="red", font=style, command=lambda: show_frame(frame_fahr))
btn_fahr.pack(side=LEFT, padx=10)

# --------- Frame 2: To Centigrade ----------
frame_cent = Frame(container)
frame_cent.place(relwidth=1, relheight=1)

Label(frame_cent, text="Enter temperature in Fahrenheit", font=("Arial", 18)).pack(pady=20)
Button(frame_cent, text="Back", command=lambda: show_frame(frame_main)).pack()

# --------- Frame 3: To Fahrenheit ----------
frame_fahr = Frame(container)
frame_fahr.place(relwidth=1, relheight=1)

Label(frame_fahr, text="Enter temperature in Centigrade", font=("Arial", 18)).pack(pady=20)
Button(frame_fahr, text="Back", command=lambda: show_frame(frame_main)).pack()

# Show main menu initially
show_frame(frame_main)

root.mainloop()