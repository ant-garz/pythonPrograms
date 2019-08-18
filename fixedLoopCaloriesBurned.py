# Author: Anthony Garza
# Purpose : To use a loop to display the amount of calories burned
# every 10, 15 , 20 , 25 and 30 min. when you burn 4.2 calories per minute

# global constants
start = 10
end = 31
increment = 5
calories_per_minute = 4.2

#format display
print('Minutes\tCalories Burned')
print('-----------------------------------')

# calculate calories burned
for time in range(start, end, increment):
    calories = time * calories_per_minute
    print(time, '\t', format(calories, '.2f'))
