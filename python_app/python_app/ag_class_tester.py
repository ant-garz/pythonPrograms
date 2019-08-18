#Script Name: ag_class_tester.py
#Author: Anthony Garza
#Purpose : to demonstrate the principles of object oriented
#           programming by using two programs testing car
#           acceleration braking. This program is the testing program
#           for this process. 

import ag_CarDefinition

def main():
    # Create an instance of Car
    my_car = ag_CarDefinition.Car("2008", "Honda Accord")

    print("my_car after instantiating:\n", my_car)

    my_car.setSpeed(2)
    print("my_car after my_car.setSpeed(2):\n", my_car)
    # accelerate 5 times
    print("My car is accelerating: ")
    for i in range(5):
        my_car.accelerate()
        print("Current speed: ", my_car.getSpeed())

    print()
    # brake 5 times
    print("Car is braking: ")
    for i in range(7):
        my_car.brake()
        print("Current speed: ", my_car.getSpeed())
        

    print("my_car values at program end:\n", my_car)

main()
