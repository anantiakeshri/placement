from tkinter import *

""" Introducing Button """
def button_clicked():
    new_text = entry.get()
    my_label.config(text=new_text)


window = Tk()
window.title("My first GUI program")
window.minsize(500, 300)
window.config(padx=20, pady=20)

# Label
my_label = Label(text="I am a Label", font=("Courier", 24, "bold"))
my_label["text"] = "New Text"
my_label.grid(column=0, row=0)

# New Button
new_button = Button(text="Here")
new_button.grid(column=2, row=0)

# Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

# Entry
entry = Entry(width=20)
entry.grid(column=3, row=2)





window.mainloop()