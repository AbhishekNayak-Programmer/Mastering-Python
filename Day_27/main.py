from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label= Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack(side='top')

my_label["text"] = "New Text"
my_label.config(text="Some Other text")

def button_clicked():
    name = input.get()
    my_label.config(text=f"Hi {name}")

button = Button(text="Click Me", command=button_clicked)
button.pack()

input = Entry(width=30)
input.pack()


window.mainloop()