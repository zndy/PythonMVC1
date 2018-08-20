#!/usr/bin/python3
from tkinter import *


class View(Frame):
    def __init__(self):
        self.frame = Frame("")
        self.frame.grid(row=0, column=0)

        self.label_text = StringVar()
        self.label_text.set('Winkel: ')
        self.entry_text = IntVar()
        self.entry_text.set(12)

        self.calcButton = Button(self.frame, text="calc", bg="yellow", fg="red")
        self.loadView()
        self.createCanvas()

    def loadView(self):
        Label(self.frame, textvariable=self.label_text).grid(row=0, column=0, columnspan=1)

        entry = Entry(self.frame, textvariable=self.entry_text)
        entry.grid(row=0, column=1, columnspan=3)
        entry.focus()

        self.calcButton.grid(row=1, column=0)

    def createCanvas(self):
        frame2 = Frame("")
        frame2.grid(row=0, column=1)
        w = Canvas(frame2, width=200, height=100)
        w.grid(row=2, column=2, columnspan=4)

        w.create_line(0, 0, 200, 100)
        w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))

        w.create_rectangle(50, 25, 150, 75, fill="blue")

    def addCalcBtnListener(self, func):
        self.calcButton.bind("<ButtonRelease-1>", func)
