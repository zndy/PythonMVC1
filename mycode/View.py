#!/usr/bin/python3
from tkinter import *


class View(Frame):
    def __init__(self):
        self.canvasFrame = Frame("")
        self.canvasFrame.grid(row=0, column=0)

        self.inputValueFrame = Frame("")
        self.inputValueFrame.grid(row=1, column=0)

        self.label_text = StringVar()
        self.label_text.set('Winkel: ')
        self.entry_text = IntVar()
        self.entry_text.set(12)

        self.calcButton = Button(self.inputValueFrame, text="calc", bg="yellow", fg="red")

        self.createCanvasFrame()
        self.createInputValueFrame()

    def createInputValueFrame(self):
        Label(self.inputValueFrame, textvariable=self.label_text).grid(row=0, column=0, columnspan=1)
        entry = Entry(self.inputValueFrame, textvariable=self.entry_text)
        entry.grid(row=0, column=1, columnspan=3)
        entry.focus()
        self.calcButton.grid(row=1, column=0)

    def createCanvasFrame(self):
        w = Canvas(self.canvasFrame, width=200, height=100)
        w.grid(row=2, column=2, columnspan=4)
        w.create_line(0, 0, 200, 100)
        w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))
        w.create_rectangle(50, 25, 150, 75, fill="blue")

    def addCalcBtnListener(self, func):
        self.calcButton.bind("<ButtonRelease-1>", func)
