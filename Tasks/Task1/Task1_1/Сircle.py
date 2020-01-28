import math #Этот импорт предоставляет возможность работать с библиотекой math для проведения математических операций

class Сircle(): #это объявления класса. Так как мы с тобой опытные программисты, мы начнём с ООП.

    def __init__(self): #Это конструктор объекта.
        self.__radius = 0

    def calculateArea(self, radius): #Функция расчёта площади круга, принимающая в качестве параметра радиус.
        return math.pi * math.pow(self.__radius, 2) #Функция возвращает число.

    def printResult(self):
        print("Площадь круга равна " + str(self.calculateArea(self.__radius)) + " см.")

    def getRadius(self):
        return self.__radius

    def setRadius(self, radius):
        self.__radius = radius