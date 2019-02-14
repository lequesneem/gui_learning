import tkinter

root = tkinter.Tk()

root.title("hello world!")
root.geometry("600x200")

my_label = tkinter.Label(root)
my_label.config(text="Hello!", fg="green")
my_label.grid()

my_label = tkinter.Label(root)
my_label.config(text="Hello there!", fg="blue")
my_label.grid()

my_label = tkinter.Label(root)
my_label.config(text="Hey you!", fg="pink")
my_label.grid()

root.mainloop()
