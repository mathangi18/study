print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("how much percentage tip would you like to give?n10 12 15"))
people = int(input("how many people to split the bill?"))
bill_with_tip = tip / 100 * bill + bill
bill_per_person = bill_with_tip / people
final_amount = round(bill_per_person, 2)
print(f"Each person has to pay $ {final_amount}")
