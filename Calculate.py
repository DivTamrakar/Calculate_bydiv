
import tkinter as tk

def calculate():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    operator = entry3.get()

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2
    else:
        result = "Invalid operator"

    label.config(text="Result: " + str(result))

root = tk.Tk()
root.title("Calculator By DIV")

entry1 = tk.Entry(root)
entry2 = tk.Entry(root)
entry3 = tk.Entry(root)

label = tk.Label(root, text="")

entry1.grid(row=0, column=0)
entry2.grid(row=0, column=1)
entry3.grid(row=0, column=2)
label.grid(row=1, column=0, columnspan=3)

button = tk.Button(root, text="Calculate", command=calculate)
button.grid(row=2, column=0, columnspan=3)

root.mainloop()
