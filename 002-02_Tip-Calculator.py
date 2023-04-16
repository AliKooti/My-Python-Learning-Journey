"""
If the bill was $150.00, split between 5 people, with 12% tip. 
Each person should pay (150.00 / 5) * 1.12 = 33.6
Format the result to 2 decimal places = 33.60
"""
print("Welcome to the tip calculator.")
bill = float(input("What is your total bill? €"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

pay_person = round((bill / people) * (1+(tip_percentage/100)),2)
print(f"Each person should pay: €{pay_person}")
