# Script Name: ag_assignment3_completed.py
# Author : Anthony Garza
# Purpose : This program is designed to take the value of the coins that
#           the user enters and counts it's value in dollars in cents.
#           It then displays the total value in dollars and shows 
#           how many dollars and leftover cents there are.


def main():
    pennies = int(input("Enter pennies : "))
    nickels = int(input("Enter nickels : "))
    dimes = int(input("Enter dimes : "))
    quarters = int(input("Enter quarters : "))
    total = (pennies * 1) + (nickels * 5) + (dimes * 10) + (quarters * 25)
    
    def get_total(pennies, nickels, dimes, quarters):
        total_pennies = pennies * 0.01
        total_nickels = nickels * 0.05
        total_dimes = dimes * 0.10
        total_quarters = quarters * 0.25
        total_amt = total_pennies + total_nickels + total_dimes + total_quarters
        return total_amt
        
    def get_dollars(pennies, nickels, dimes, quarters):
        dollars = int(total / 100)
        return dollars
    def get_left_over_cents(pennies, nickels, dimes, quarters):
        cents = total %100
        return cents


    print("You entered : ")
    print("\tPennies  : " , pennies)
    print("\tNickels  : " , nickels)
    print("\tDimes    : " , dimes)
    print("\tQuarters : " , quarters)

    total_value = get_total(pennies, nickels, dimes, quarters)
    dollars = get_dollars(pennies, nickels, dimes, quarters)
    left_over_cents = get_left_over_cents(pennies, nickels, dimes, quarters)


    print("Total = $", format(total_value, '.2f'), sep="")
    print("You have", dollars, "dollars and", left_over_cents, "cent(s)")
    

main()

#the comment lines below indicate my two test data sets

#>>> ================================ RESTART ================================
#>>> 
#Enter pennies : 23
#Enter nickels : 3
#Enter dimes : 4
#Enter quarters : 3
#You entered :
#	Pennies  :  23
#	Nickels  :  3
#	Dimes    :  4
#	Quarters :  3
#Total = $1.53
#You have 1 dollars and 53 cent(s)
#>>> ================================ RESTART ================================
#>>> 
#Enter pennies : 0
#Enter nickels : 3
#Enter dimes : 4
#Enter quarters : 3
#You entered : 
#	Pennies  :  0
#	Nickels  :  3
#	Dimes    :  4
#	Quarters :  3
#Total = $1.30
#You have 1 dollars and 30 cent(s)
#>>> 



