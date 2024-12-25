print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

amount_to_pay = (float(bill * float(tip / 100) + bill ) / people)

print(amount_to_pay)