# author Sandro Skhirtladze

from tkinter import *
import math

window = Tk()
window.geometry("420x250")
window.title("Quadratic Equation Solver")
titleLabel = Label(window, text="Solve Equation for x", font=("arial", 16, "bold")).pack()


def solveEquation():
    try:
        a = float(inputA.get())
        b = float(inputB.get())
        c = float(inputC.get())
        D = b ** 2 - (4 * a * c)
        try:
            d = math.sqrt(D)
            x1 = format((((-1) * b) + d) / (2 * a), '.4f')
            x2 = format((((-1) * b) - d) / (2 * a), '.4f')
            answer.config(text="x1 = " + x1 + "     x2 = " + x2)
        except ValueError:
            answer.config(text="Discriminant is negative")
    except ValueError:
        answer.config(text="Please Input Numbers")


solveButton = Button(window,
                     text="Solve",
                     fg="white",
                     bg="#27ae60",
                     cursor="hand2",
                     font=("arial", 15),
                     borderwidth=0,
                     command=solveEquation
                     ).place(relx=0.5, y=155, anchor=CENTER)
inputA = Entry(window, width=10)
inputA.place(x=50, y=100)
x2Label = Label(window, text="x² + ", font=("arial", 16)).place(x=118, y=94)
inputB = Entry(window, width=10)
inputB.place(x=162, y=100)
xLabel = Label(window, text="x + ", font=("arial", 16)).place(x=230, y=94)
inputC = Entry(window, width=10)
inputC.place(x=268, y=100)
xLabel = Label(window, text=" = 0 ", font=("arial", 15)).place(x=332, y=94)
answer = Label(window, text="ans", font=("arial", 15))
answer.place(relx=0.5, y=194, anchor=CENTER)
window.mainloop()
