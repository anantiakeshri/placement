from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(500, 300)

my_label = Label(text="I am a Label", font=("Courier", 24, "bold"))
my_label.pack()

my_label["text"] = "New Text"
my_label.pack()

""" Introducing Button """
def button_clicked():
    new_text = entry.get()
    my_label.config(text=new_text)


button = Button(text="Click Me", command=button_clicked)
button.pack()


""" Introducing Entry"""
entry = Entry(width=20)
entry.pack()





window.mainloop()