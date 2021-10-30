#!/usr/bin/python3

# import non-stdlib libraries
import tkinter as tk
from functools import partial

# initialising constant list of buttons
buttons = [["7", "8", "9", " * "], ["4", "5", "6", " / "], ["1", "2", "3", " + "], ["0", "=", "CE", " - "]]

# calculator class - i used object-oriented programming to avoid using global variables
class Calculator():
    # initialisation function to create class calculation variable
    def __init__(self):
        self.calculation = ""
    # callback function when button is pressed, callback functions are usually invoked when an action is completed
    def callback(self, value, operator=None):
        # checks that = button has been pressed
        if value == "=":
            try:
                # changes label to show calculation result
                self.lbl['text'] = eval(self.calculation)
                self.calculation = str(eval(self.calculation))
            except Exception:
                # error message if calculation is not valid
                self.lbl['text'] = "ERROR"
                self.calculation = ""
        # checks that CE button has been pressed
        elif value == "CE":
            # resets text in label and calculation variable
            self.lbl['text'] = ""
            self.calculation = ""
        else:
            self.calculation += value
            self.lbl['text'] = self.calculation
        # returns calculation variable once button has been pressed and the result is processed
        return self.calculation

    # procedure to make tkinter GUI
    def makeGUI(self):
        # creates an instance of tk class
        root = tk.Tk()
        
        # creates buttons from list initialised earlier
        for i in range(len(buttons)):
            for j in range(len(buttons[i])):
                # partial function allows us to add parameters to the function call when button is pressed by creating a new function (which calls the callback function)
                btn = tk.Button(root, text=buttons[i][j], command=partial(self.callback, buttons[i][j]), width=5)
                btn.grid(column=j+1, row=i+1)
        
        # window showing calculation
        self.lbl = tk.Label(root, text="", height=2)
        self.lbl.grid(column=0, row=0, columnspan=5)

        root.mainloop()

# creating instance of Calculator class
calc = Calculator()
# calls makeGUI function, otherwise nothing will happen
calc.makeGUI()
