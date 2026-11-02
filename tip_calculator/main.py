def tip_calculator():
    bill = float(input("how much is the bill"))
    people = int(input("How many people are there"))
    tip_percentage = float(input("how much would you like to tip in perentages"))
    total_tip = (tip_percentage/100) * bill
    total_bill = bill + total_tip
    bill_per_person = round(total_bill/people, 2)
    return bill_per_person




print("welcome to the tip calculator")
print(tip_calculator())

    