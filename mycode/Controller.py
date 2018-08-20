#!/usr/bin/python3
from mycode.Model import *
from mycode.View import *
from tkinter import messagebox


class Controller2:
    def __init__(self):
        self.model = Model()
        self.view = View()
        self.view.addCalcBtnListener(self.calcButtonPressed)

    def calcButtonPressed(self, event):
        self.model.setAngle(self.view.angleEntry.get())
        self.model.setPa1(self.view.pa1Entry.get())
        self.model.setPa2(self.view.pa2Entry.get())
        print("result = " + self.model.calc())
        messagebox.showinfo('Message title', self.model.calc())


def main():
    window = Tk()  # create a Tk root window
    window.title('Abrichten')
    w = 800  # width for the Tk root
    h = 650  # height for the Tk root

    # get screen width and height
    ws = window.winfo_screenwidth()  # width of the screen
    hs = window.winfo_screenheight()  # height of the screen

    # calculate x and y coordinates for the Tk root window
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)

    # set the dimensions of the screen
    # and where it is placed
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))
    Controller2()
    window.mainloop()


if __name__ == '__main__':
    main()
