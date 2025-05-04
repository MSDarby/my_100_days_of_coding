print("Welcome to the tip calculator!")
bill = float(input("What was the total bill?: £"))
tip = input("How much tip would you like to give? 10, 12, 15 n.b. please dont add a % sign: ")
tip_percent = float(tip)/100
total = bill + (bill * tip_percent)
people = int(input("how many people to split the bill?: "))

bill_per_person = round(total / people, 2)
bill_per_person = "{:.2f}".format(bill_per_person)

print(f"Each person should pay: £{bill_per_person}")
