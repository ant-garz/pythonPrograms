# Script Name: ag_assignment2_completed.py
# Author : Anthony Garza
# Purpose : The purpose of this program is to utilize loop structures to
#           calcuate distance traveled by multiplying traveling speed by
#           the number of hours traveled. 

#data input and validation
vehicle_speed = int(input('What is the speed of the vehicle in mph? :'))
while vehicle_speed < 0:
    print('Invalid Entry! Speed must be greater than 0')
    vehicle_speed = int(input('What is the speed of the vehicle in mph? :'))
    
hours_traveled = int(input('How many hours has it traveled?'))

while hours_traveled < 0:
    print('Invalid Entry! Hours must be greater than 0')
    hours_traveled = int(input('How many hours has it traveled?'))
    

#display input data
while vehicle_speed > 0 and hours_traveled > 0:
    print('Hours Traveled:', hours_traveled, '\t', 'Speed in Mph:', vehicle_speed)
    print('Hours\tDistance Traveled')
    print('-------------------------------')
    break

#calculating distance traveled
for hours_traveled in range(1, hours_traveled + 1):
    distance_traveled = hours_traveled * vehicle_speed
    print(hours_traveled, '\t', distance_traveled)

# my data sets

#>>> ================================ RESTART ================================
#>>> 
#What is the speed of the vehicle in mph? : -25
#Invalid Entry! Speed must be greater than 0
#What is the speed of the vehicle in mph? : -30
#Invalid Entry! Speed must be greater than 0
#What is the speed of the vehicle in mph? : -50
#Invalid Entry! Speed must be greater than 0
#What is the speed of the vehicle in mph? : 25
#How many hours has it traveled? -5 
#Invalid Entry! Hours must be greater than 0
#How many hours has it traveled? -10
#Invalid Entry! Hours must be greater than 0
#How many hours has it traveled? 5
#Hours Traveled: 5 	 Speed in Mph: 25
#Hours	Distance Traveled
#-------------------------------
#1 	 25
#2 	 50
#3 	 75
#4 	 100
#5 	 125
#>>> ================================ RESTART ================================
#>>> 
#What is the speed of the vehicle in mph? : -45
#Invalid Entry! Speed must be greater than 0
#What is the speed of the vehicle in mph? : -40
#Invalid Entry! Speed must be greater than 0
#What is the speed of the vehicle in mph? : -30
#Invalid Entry! Speed must be greater than 0
#What is the speed of the vehicle in mph? : 30
#How many hours has it traveled? -343
#Invalid Entry! Hours must be greater than 0
#How many hours has it traveled? -5
#Invalid Entry! Hours must be greater than 0
#How many hours has it traveled? 4
#Hours Traveled: 4 	 Speed in Mph: 30
#Hours	Distance Traveled
#-------------------------------
#1 	 30
#2 	 60
#3 	 90
#4 	 120
#>>> 
