import tkinter

root = tkinter.Tk()

def print_emma():
    print("Emma")

button1 = tkinter.Button(root)
button1.config(text="Click to see Emma",
               bg="white",
               fg="light blue",
               font=("nunito", "50"),
               command = print_emma)

button1.grid()

root.mainloop()
