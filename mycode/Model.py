#!/usr/bin/python3


class Model:
    def __init__(self):
        self.__angle = 0
        self.__pa1 = 0
        self.__pa2 = 0

    def getAngle(self):
        return self.__angle

    def setAngle(self, angle):
        self.__angle = angle

    def getPa1(self):
        return self.__pa1

    def setPa1(self, pa1):
        self.__pa1 = pa1

    def getPa2(self):
        return self.__pa2

    def setPa2(self, pa2):
        self.__pa2 = pa2

    def calc(self):
        return "angle= " + str(self.__angle) +\
               " pa1 =" + str(self.__pa1) +\
               " pa2 =" + str(self.__pa2)
