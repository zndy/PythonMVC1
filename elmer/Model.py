#!/usr/bin/python3


class Model:
    def __init__(self):
        self.__angle = 0

    def setAngle(self, angle):
        self.__angle = angle

    def getAngle(self):
        return self.__angle

    def calc(self):
        return self.__angle ** 2
