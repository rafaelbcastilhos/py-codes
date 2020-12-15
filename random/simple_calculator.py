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



