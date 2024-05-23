from evaluator import *
from tkinter import *

root = Tk()
variables = []
variable_names = []
text_input = StringVar()
result_text = StringVar(value="Invalid input")

def display_variables(exp_text):
    global variable_names, variables
    variable_names = variable_detector(exp_text)
    while len(variable_names) > len(variables):
        variables.append(IntVar(value=0))

    for widget in root.grid_slaves():
        if int(widget.grid_info()["row"]) < 10 and int(widget.grid_info()["row"]) >= len(variable_names):
            widget.grid_forget()

    for i in range(len(variable_names)):
        Label(root, text=variable_names[i]).grid(row=i, column=0)
        Radiobutton(root, text='True', variable=variables[i], value=1, command=update_result).grid(row=i, column=1)
        Radiobutton(root, text='False', variable=variables[i], value=0, command=update_result).grid(row=i, column=2)

def update_result(*args):
    display_variables(text_input.get())
    var_values = [var.get() for var in variables]
    result = evaluate_expression(text_input.get(), variable_names, var_values)
    if result == 1:
        result_text.set("True")
        result_label = Label(root, textvariable=result_text, fg='green').grid(row=10, column=3)
        root.update()
    elif result == 0:
        result_text.set("False")
        result_label = Label(root, textvariable=result_text, fg='red').grid(row=10, column=3)
        root.update()
    else: #result == -1, error
        result_text.set("Invalid Input")
        result_label = Label(root, textvariable=result_text, fg='red').grid(row=10, column=3)
        root.update()
    

root.minsize(300, 200)
text_input.trace_add("write", update_result)
input_label = Label(root, text='Input Text').grid(row=10, column=0)
input_entry = Entry(root, textvariable=text_input).grid(row=10, column=1)
result_label = Label(root, textvariable=result_text, fg='red').grid(row=10, column=3)
root.mainloop()
