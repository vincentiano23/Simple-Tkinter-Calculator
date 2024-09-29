from tkinter import *

root = Tk()
root.title("Simple Calculator App")

# Add some padding and window size
root.geometry("350x400")
root.config(bg="#e0f7fa")

ew = Entry(root, width=40, borderwidth=5)
ew.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Global variable to store current expression
expression = ""


def button_click(number):
    """Add the clicked number to the current expression."""
    global expression
    expression += str(number)
    ew.delete(0, END)
    ew.insert(0, expression)


def button_clear():
    """Clear the current entry."""
    global expression
    expression = ""
    ew.delete(0, END)


def button_equal():
    """Evaluate the current expression."""
    global expression
    try:
        result = str(eval(expression))  # Use eval to calculate the result
        ew.delete(0, END)
        ew.insert(0, result)
        expression = result  # Update the expression with the result
    except:
        ew.delete(0, END)
        ew.insert(0, "Error")
        expression = ""


def button_add():
    button_click("+")


def button_subtract():
    button_click("-")


def button_multiply():
    button_click("*")


def button_divide():
    button_click("/")


# Define buttons with improved styling
button_1 = Button(root, text="1", padx=30, pady=20, bg="#b2dfdb", command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=30, pady=20, bg="#b2dfdb", command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=30, pady=20, bg="#b2dfdb", command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=30, pady=20, bg="#b2dfdb", command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=30, pady=20, bg="#b2dfdb", command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=30, pady=20, bg="#b2dfdb", command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=30, pady=20, bg="#b2dfdb", command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=30, pady=20, bg="#b2dfdb", command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=30, pady=20, bg="#b2dfdb", command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=30, pady=20, bg="#b2dfdb", command=lambda: button_click(0))

button_add = Button(root, text="+", padx=30, pady=20, bg="#80cbc4", command=button_add)
button_subtract = Button(root, text="-", padx=32, pady=20, bg="#80cbc4", command=button_subtract)
button_multiply = Button(root, text="*", padx=32, pady=20, bg="#80cbc4", command=button_multiply)
button_divide = Button(root, text="/", padx=32, pady=20, bg="#80cbc4", command=button_divide)
button_clear = Button(root, text="Clear", padx=60, pady=20, bg="#ffccbc", command=button_clear)
button_equals = Button(root, text="=", padx=80, pady=20, bg="#ffab91", command=button_equal)

# Put buttons on the screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)

button_clear.grid(row=4, column=1, columnspan=2)
button_add.grid(row=5, column=0)
button_equals.grid(row=5, column=1, columnspan=2)

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

root.mainloop()
