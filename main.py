print('Welcome to the tip calculator.')
# input the price
total_bill = float(input("What was the total bill?\n"))
# input the perccenatge tip
percentage = int(input("What percentage tip would you like to give? 10%, 12% or 15%?\n"))
# input to how many ways to split the price
split = int(input("How many people to split the bill?\n"))
# calculate the percentage tip
tip = total_bill * (percentage/100)
# the new total price with the tip
total_price = total_bill + tip
# individual pay amount
individual_pay = round(total_price/split,2)
print(f"Each person should pay: {individual_pay}")
