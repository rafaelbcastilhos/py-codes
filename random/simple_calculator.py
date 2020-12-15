# simple calculator using tkinter gui
from tkinter import *


# function calculates the operations
def calculates():
    which_button = selected_operation.get()
    value_1 = float(entry_field_1.get())
    value_2 = float(entry_field_2.get())
    if which_button == 1:
        result = value_1 + value_2
    elif which_button == 2:
        result = value_1 - value_2
    elif which_button == 3:
        result = value_1 * value_2
    elif which_button == 4:
        result = value_1 / value_2

    result_field.delete(0, END)
    result_field.insert(0, result)


root = Tk()
# header
root.title("simple calculator")
window_title = Label(root, text="simple calculator", font=("Helvetica", 14)).grid(row=0, column=0, columnspan=2)

# number 1 and 2
label_1 = Label(root, text="enter a number").grid(row=1, column=0)
entry_field_1 = Entry(root, text="number 1", width=10)
entry_field_1.grid(row=1, column=1)
label_2 = Label(root, text="enter a number").grid(row=2, column=0)
entry_field_2 = Entry(root, text="number 2", width=10)
entry_field_2.grid(row=2, column=1)

# operation
selected_operation = IntVar()
label_3 = Label(root, text="choose the operation").grid(row=3, column=0, columnspan=2)

# buttons
# sum
sum_button = Radiobutton(root, text="+", variable=selected_operation, value=1)
sum_button.grid(row=4, column=0)
# subtraction
subtraction_button = Radiobutton(root, text="-", variable=selected_operation, value=2)
subtraction_button.grid(row=4, column=1)
# multiplication
multiplication_button = Radiobutton(root, text="x", variable=selected_operation, value=3)
multiplication_button.grid(row=5, column=0)
# division
division_button = Radiobutton(root, text="/", variable=selected_operation, value=4)
division_button.grid(row=5, column=1)

# result
button = Button(root, text="calculate", command=calculates, width="30").grid(row=6, column=0, columnspan=2)
label_4 = Label(root, text="result").grid(row=7, column=0)
result_field = Entry(root)
result_field.grid(row=7, column=1)

root.mainloop()
