#i am learning python from scratch

#monthly grocery shop
groceries = {"milo" : 13.45, "sugar" : 8.50, "nido" : 15.49, "gari" : 2.50, "croissant" : 1.50}

max_quantity = 10

print("Enter your name")
name = input()
 
print(f"Welcome {name}") 

print("which items do you want to buy")
customer_list = input()

print("How many do you want to buy")
quantity = int(input())
 
bill = groceries[customer_list] * quantity

if customer_list in groceries and quantity <= max_quantity:
   print(f"Your bill is {bill}")
elif customer_list in groceries and quantity > max_quantity:
   print("Sorry we have few quantity in stock")
else:
   print("sorry kindly check the list and select accordingly")








