##Author:Maya Tolappa
##Purpose: Program for Test 3.

def main():
    sales_amount = getSalesAmount()
    tax_rate = getTaxRate()
    total_amount = getTotalAmount(sales_amount, tax_rate)
    print("Sales Amount = $", format(sales_amount, '.2f'), sep='')
    print("Tax rate     = ", format(tax_rate, '.2f'), "%", sep='')
    print("Total amount = $", format(total_amount, '.2f'), sep='')

def getSalesAmount():
    s_amount = float(input("Enter sales Amount:"))
    return s_amount

def getTaxRate():
    t_rate = float(input("Enter Tax rate as a percent, such as 6.25 or 10:"))
    return t_rate

def getTotalAmount(sales_amount, tax_rate):
    total_tax = (sales_amount * tax_rate) * .01
    total_amount = sales_amount + total_tax
    return total_amount
    
main()

#I am not sure whether or not I should edit the author and purpose in accordance with the programming standards, as it is the code you wrote for this test
# the script name, however, is now : ag_test3_hands_on.py
