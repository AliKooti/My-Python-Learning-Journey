"""
If the bill was $150.00, split between 5 people, with 12% tip. 
Each person should pay (150.00 / 5) * 1.12 = 33.6
Format the result to 2 decimal places = 33.60
"""
print("Welcome to the tip calculator.")
bill = float(input("What is your total bill? €"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

total_bill = tip/100*bill + bill
pay_person = round(total_bill/people,2)
pay_person = "{:.2f}".format(pay_person)
print(f"Each person should pay: €{pay_person}")
