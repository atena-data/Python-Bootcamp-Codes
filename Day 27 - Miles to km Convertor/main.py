from tkinter import *


def conversion():
    calculate = round(float(input_box.get()) * 1.60934, 2)
    result.config(text=calculate)


# generate a screen
window = Tk()
window.title("Unit Conversion Tool")
window.minsize(width=350, height=250)
window.config(padx=10, pady=10)

# create labels
miles = Label(text="Miles", font=("Arial", 14, "bold"))
miles.grid(column=2, row=0)
miles.config(padx=20, pady=20)

km = Label(text="Km", font=("Arial", 14, "bold"))
km.grid(column=2, row=1)
km.config(padx=20, pady=20)

covert = Label(text="is equal to", font=("Arial", 14, "bold"))
covert.grid(column=0, row=1)
covert.config(padx=20, pady=20)

result = Label(text=0, font=("Arial", 14, "bold"))
result.grid(column=1, row=1)
result.config(padx=20, pady=20)

# set a button
button = Button(text="Calculate", command=conversion)
button.grid(column=1, row=2)
button.config(padx=10, pady=10)

# set an input field
input_box = Entry(width=10)
print(input_box.get())
input_box.grid(column=1, row=0)

window.mainloop()
