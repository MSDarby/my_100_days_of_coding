from coffeemachine_data import menu 

#Starting resources
water = 300
milk = 200
coffee = 100
money = 0

def report_output(wat_amt, mil_amt, cof_amt, mon_tot): 
    return f"Water: {wat_amt}ml \nMilk: {mil_amt}ml \nCoffee: {cof_amt}g \nMoney: ${mon_tot}"

def check_resources(option, wat_amt, mil_amt, cof_amt, mon_tot): 
    

#The machine is coin operated with 1 cents = $0.01, 5 cents = $0.05, 
# 10 cents = $0.1 and 25 cents = $0.25
coins = [1, 5, 10, 25]

#What should the machine be able to do" 
# 1 - print report of how much resource it has left 
# 2 - check that resources are sufficient when 
# 3 - should be able to process coins 
# 4 - check transaction is successful 
# 5 - Make coffee 

#The machien makes 3 flavours 1. Espresso, 2. Latte, 3.Cappuccino 
1 = "espresso"
2 = "latte"
3 = "cappuccino"

option=int(input('What would you like? Type 1 - espresso, 2 - latte or  3 - cappuccino): \n'))

if option not in  [1, 2, 3]:
    print ("Invalid option selected, please try again.")
elif option == 1: 
    print(report_output(water, milk, coffee, money))

