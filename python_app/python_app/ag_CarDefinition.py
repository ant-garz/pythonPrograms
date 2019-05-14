#Script Name: ag_CarDefinition.py
#Author: Anthony Garza
#Purpose: To demonstrate the principles of object oriented programming
#         by using the two programs testing car acceleration and braking. This
#         program is the one that defines the class "Car" and is used in the
#         test program. This is one of two programs to satisfy the requirements
#         for lab 4.

class Car:
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    ############# year_model################
    def setYear_model(self, year_model):
        self.__year_model = year_model

    def getYear_model(self):
        return self.__year_model

    ############# Make################
    def setMake(self, make):
        self.__make = make

    def getMake(self):
        return self.__make

    ############# speed################
    def setSpeed(self, speed):
        if speed < 0:
            print("Speed cannot be negative")
        else:
            self.__speed = speed

    def getSpeed(self):
        return self.__speed

    ############# str ############
    def __str__(self):
        return "Make : " + self.__make + ", Model Year :" + \
            self.__year_model + ", speed =" + str(self.__speed)
    
    ############# coding for acceleration function #####
    def accelerate(self):
        while self.__speed >= 0:
                self.__speed = self.__speed + 5
                break
                
    ############ coding for brake function #############
    def brake(self):
        self.__speed = self.__speed - 5
        while self.__speed < 0:
            print("Error! Speed must be greater than 0, resetting to 0")
            self.__speed = 0
         
            
            


