import sys
print(sys.version)

#simple Expense Tracker 
name = input("What is your name? ")
print(f"Hello, {name}!")

weekly_budget = float(input("What is your weekly budget? "))

print("Enter expense 1 : ")
expense1 = float(input())
print("Enter expense 2 : ")
expense2 = float(input())
print("Enter expense 3 : ")
expense3 = float(input())

print(f"Your budget was : ${weekly_budget}")

total_expenses = expense1 + expense2 + expense3
print(f"you spent: ${total_expenses}")

Balance = weekly_budget - total_expenses
print(f"You have ${Balance} left")
