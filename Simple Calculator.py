from tkinter import *

root = Tk()
enter = Entry(root, width=25, borderwidth=4)
enter.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def press(x: int) -> None:
    # snapshot of current entries
    current = enter.get()
    # clear the box
    enter.delete(0, END)
    # current entries plus input
    enter.insert(0, str(current) + str(x))

def clear_button():
    enter.delete(0, END)


def addition():
    first_number = enter.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    enter.delete(0, END)


def subtraction():
    first_number = enter.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    enter.delete(0, END)


def growth():
    first_number = enter.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    enter.delete(0, END)


def cutting():
    first_number = enter.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    enter.delete(0, END)


def execute():
    second_number = int(enter.get())
    enter.delete(0, END)
    if math == "addition":
        enter.insert(0, f_num + second_number)
    elif math == "subtraction":
        enter.insert(0, f_num - second_number)
    elif math == "multiplication":
        enter.insert(0, f_num * second_number)
    else:
        enter.insert(0, f_num / second_number)


one = Button(root, text="1", padx=40, pady=20, command=lambda: press(1))
two = Button(root, text="2", padx=40, pady=20, command=lambda: press(2))
three = Button(root, text="3", padx=40, pady=20, command=lambda: press(3))
four = Button(root, text="4", padx=40, pady=20, command=lambda: press(4))
five = Button(root, text="5", padx=40, pady=20, command=lambda: press(5))
six = Button(root, text="6", padx=40, pady=20, command=lambda: press(6))
seven = Button(root, text="7", padx=40, pady=20, command=lambda: press(7))
eight = Button(root, text="8", padx=40, pady=20, command=lambda: press(8))
nine = Button(root, text="9", padx=40, pady=20, command=lambda: press(9))
zero = Button(root, text="0", padx=40, pady=20, command=lambda: press(0))
plus = Button(root, text="+", padx=39, pady=20, command=addition)
minus = Button(root, text="-", padx=39, pady=20, command=subtraction)
multiply = Button(root, text="*", padx=39, pady=20, command=growth)
divide = Button(root, text="/", padx=39, pady=20, command=cutting)
equal_sign = Button(root, text="=", padx=87, pady=20, command=execute)
clear = Button(root, text="clear", padx=79, pady=20, command=clear_button)

one.grid(row=1, column=0)
two.grid(row=1, column=1)
three.grid(row=1, column=2)
four.grid(row=2, column=0)
five.grid(row=2, column=1)
six.grid(row=2, column=2)
seven.grid(row=3, column=0)
eight.grid(row=3, column=1)
nine.grid(row=3, column=2)
zero.grid(row=4, column=0)
clear.grid(row=4, column=1, columnspan=2)
equal_sign.grid(row=5, column=1, columnspan=2)
plus.grid(row=5, column=0)
multiply.grid(row=6, column=1)
minus.grid(row=6, column=0)
divide.grid(row=6, column=2)

root.mainloop()