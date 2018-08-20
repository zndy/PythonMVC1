#!/usr/bin/python3
from tkinter import *


class View(Frame):
    def __init__(self):
        self.canvasFrame = Frame("")
        self.canvasFrame.grid(row=0, column=0)
        self.inputValueFrame = Frame("")
        self.inputValueFrame.grid(row=1, column=0)


        self.angleEntry = IntVar()
        self.angleEntry.set(12)
        self.pa1Entry=IntVar()
        self.pa2Entry=IntVar()

        self.calcButton = Button(self.inputValueFrame, text="calc", bg="yellow", fg="red")

        self.__createCanvasFrame()
        self.__createInputValueFrame()

    def __createInputValueFrame(self):
        Label(self.inputValueFrame, text='Angle: ').grid(row=0, column=0, columnspan=1)
        entry = Entry(self.inputValueFrame, textvariable=self.angleEntry)
        entry.grid(row=0, column=1, columnspan=3)
        entry.focus()

        Label(self.inputValueFrame, text='Pa1: ').grid(row=1, column=0, columnspan=1)
        Entry(self.inputValueFrame, textvariable=self.pa1Entry).grid(row=1, column=1, columnspan=3)

        Label(self.inputValueFrame, text='Pa2: ').grid(row=2, column=0, columnspan=1)
        Entry(self.inputValueFrame, textvariable=self.pa2Entry).grid(row=2, column=1, columnspan=3)

        self.calcButton.grid(row=10, column=0)

    def __createCanvasFrame(self):
        w = Canvas(self.canvasFrame, width=200, height=100)
        w.grid(row=2, column=2, columnspan=4)
        w.create_line(0, 0, 200, 100)
        w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))
        w.create_rectangle(50, 25, 150, 75, fill="blue")

    def addCalcBtnListener(self, func):
        self.calcButton.bind("<ButtonRelease-1>", func)
