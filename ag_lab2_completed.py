# Script Name : ag_lab2_completed.py
# Author : Anthony Garza (CIS115: Introduction to Programming)
#Purpose : To take the weight, in lbs, of an item given as input
#          from the program user to calculate it's shipping cost.
#          The price of the shipping cost depends on the weight of the
#          item. It's shipping cost will be determined by multiplying
#          it's weight in lbs. by a certain $ amount depending on the
#          weight of said item.

# Local variables
weight = 0.0
shippingCost = 0.0

# Get package weight from the user.
weight = float(input('Enter the weight of the package: '))


#format the weight to 2 decimal places
weight_fmt = format(weight, '.2f')

# Calculate the shipping charge.
lessthan2 = weight * 1.50
over2notmorethan6 = weight * 3.00
over6notmorethan10 = weight * 4.00
over10 = weight * 4.75

#format the shipping charge to 2 decimal places
lessthan2_fmt = format(lessthan2, '.2f')
over2notmorethan6_fmt = format(over2notmorethan6, '.2f')
over6notmorethan10_fmt = format(over6notmorethan10, '.2f')
over10_fmt = format(over10, '.2f')

# Display the shipping charge.
if weight < 2:
    print('weight = ', weight_fmt, 'lbs.')
    print('Shipping Charge: $', lessthan2_fmt)
elif weight >2 and weight <= 6:
    print('weight = ', weight_fmt, 'lbs.')
    print('Shipping Charge: $', over2notmorethan6_fmt)
elif weight >6 and weight <=10:
    print('weight =', weight_fmt, 'lbs.')
    print('Shipping Charge: $', over6notmorethan10_fmt)
else:
    print('weight =', weight_fmt, 'lbs.')
    print('Shipping Charge: $', over10_fmt)

# My two test-data entries into this program

# my first input shown below: weight of the package at 343
#Enter the weight of the package: 343
#weight = 343.00 lbs.
#Shipping Charge: $ 1629.25

# my second input shown below: weight of the package at 5.55
#Enter the weight of the package: 5.55
#weight =  5.55 lbs.
#Shipping Charge: $ 16.65

    
    
