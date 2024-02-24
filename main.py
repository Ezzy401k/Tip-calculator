print('Welcome to the tip calculator.')
# input the price
total_bill = float(input("What was the total bill?\n"))
# input the percentage tip
percentage = int(input("What percentage tip would you like to give? 10%, 12% or 15%?\n"))
# Input to how many ways to split the price
split = int(input("How many people to split the bill?\n"))
# calculate the percentage tip
tip = total_bill * (percentage/100)
# The new total price with the tip
total_price = total_bill + tip
# Individual pay amount rounded to 2 decimal numbers
individual_pay = "{:.2f}".format(total_price/split)
print(f"Each person should pay: {individual_pay}")
