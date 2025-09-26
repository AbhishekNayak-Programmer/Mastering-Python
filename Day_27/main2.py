from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label= Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.place(x=100, y=50)

my_label["text"] = "New Text"
my_label.config(text="Some Other text")

def button_clicked():
    name = input.get()
    my_label.config(text=f"Hi {name}")

button = Button(text="Click Me", command=button_clicked)
button.place(x=100, y=150)

input = Entry(width=30)
input.place(x=100, y=250)

window.mainloop()