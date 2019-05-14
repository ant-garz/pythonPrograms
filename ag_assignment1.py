# Script Name : ag_assignment1.py
# Author : Anthony Garza (CIS115 : Introduction to Programming)
# Purpose : This program computes the Total Price of an item given the
#           item's original purchase price. From the purchase price it
#           computes the item's county and state sales tax, and adds the
#           sum of both taxes along with the purchase price to give the
#           user of the program that item's total price.
#
# ask user to enter purchase price and store in the purchase price variable.    

purchaseprice = float(input('Enter Purchase Price : '))

# Calculate the County and the State Sales Tax.
County_Sales_Tax = purchaseprice * .025
State_Sales_Tax = purchaseprice * .05

#Calculate Total Tax on Sale

Total_Tax = County_Sales_Tax + State_Sales_Tax

#Calculate Total Price
Total_Price = purchaseprice + Total_Tax


#Format variables to 2 places after the decimal

countytax_fmt = format(County_Sales_Tax, '.2f')
statetax_fmt = format(State_Sales_Tax, '.2f')
totaltax_fmt = format(Total_Tax, '.2f')
totalprice_fmt = format(Total_Price, '.2f')

#Print the results of the program
print('Purchase Price= $', purchaseprice)
print('State Sales Tax= $', statetax_fmt,'(5% of Purchase Price)')
print('County Tax = $', countytax_fmt, '(2.5% of Purchase Price)')
print('Total Tax = $', totaltax_fmt)
print('Total Price = $', totalprice_fmt)
