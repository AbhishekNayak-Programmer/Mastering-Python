from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label= Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)

my_label["text"] = "New Text"
my_label.config(text="Some Other text")

def button_clicked():
    name = input.get()
    my_label.config(text=f"Hi {name}")

button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

input = Entry(width=30)
input.grid(column=2, row=2)

window.mainloop()