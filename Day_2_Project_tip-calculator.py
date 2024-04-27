print("Welcome to the tip calcular")
bill = int(input("What was the total bill?: "))
tip = input("How much tip would you like to give? 10, 12, 15: ")
tip_percent = int(tip)/100
total = bill + (bill * tip_percent)
people = int(input("how many people to split the bill?: "))

split = round(total / people, 2)

print("Each person should pay: $" + str(split))