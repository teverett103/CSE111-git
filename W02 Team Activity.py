# Authors: Joseph Carlson, Taylor Everett, Sam Hopkins, Gerardo Plata
# Purpose: To calculate sales totals and discounts depending on day. 

# Retrieve date for sale and variables.
from datetime import datetime
current_date_and_time = datetime.now()
day_of_week = current_date_and_time.weekday()

# Variables and Loop to do sales calculations.
subtotal = 1

while subtotal != 0:
    subtotal = float(input('Please enter the subtotal: '))
    sales_tax = .06 * subtotal
    discount_amount = .10 * subtotal
    total_no_discount = subtotal + sales_tax
    total_with_discount = (total_no_discount - discount_amount)
    discount_subtotal = subtotal - discount_amount 
    discount_sales = discount_subtotal * .06
    discount_sales_total = discount_subtotal + discount_sales

#Prints the Discount amout, Sales tax, and grand total of discounted amount.
    if subtotal >= 50 and day_of_week == 1 or day_of_week == 2:
        print(f'Discount amount: {discount_amount:.2f}')
        print(f'Sales tax amount: {discount_sales:.2f}')
        print(f'Total: {discount_sales_total:.2f}')


#Prints the sales tax amount, and the total without a discount
    else:
        print(f"Sales tax amount: {sales_tax:.2f}")
        print(f"{total_no_discount:.2f}")
