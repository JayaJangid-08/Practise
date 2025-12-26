'''
Input we need
        -> Total rent
        -> Total food ordered
        -> Electricity units spend 
        -> Charges per unit
'''
'''
Output
    ->Total amount yo've to pay is
'''
input("Welcome to Rent Calculator\nPress Enter to continue")
total_rent = int(input("Enter the total rent amount: "))
total_food = int(input("Enter the total food ordered amount: "))
electricity_units = int(input("Enter the electricity units spent: "))
charge_per_unit = int(input("Enter the charges per unit of electricity: "))
Persons = int(input("Enter the number of persons sharing the rent: "))

total_bill = electricity_units * charge_per_unit
output = (total_rent + total_food + total_bill) // Persons
print(f"The total amount you've to pay is: {output}")
