import tkinter

root = tkinter.Tk()

root.title("hello world!")
root.geometry("600x200")

my_label = tkinter.Label(root)
my_label.config(text="Emma!", fg="white", bg="orange", font=("nunito", "70", "italic"))
my_label.grid()

my_label = tkinter.Label(root)
my_label.config(text="Emma!", fg="pink", bg="white", font=("Stencil", "70"), padx="20")
my_label.grid()

my_label = tkinter.Label(root)
my_label.config(text="Emma!", fg="purple", bg="light blue", font=("Times", "70", "bold"), pady="30")
my_label.grid()

root.mainloop()
