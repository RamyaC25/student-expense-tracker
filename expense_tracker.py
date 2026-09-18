user_budget = int(input("Enter your budget: "))
user_expense = int(input("Enter your expense: "))
category = input("Enter the expense category: ")
description = input("Enter the expense description: ")
print("--- Expense Details ---")
print("Category: " + category)
print("Description: " + description)
print("Amount: " + str(user_expense))
print("-----------------------")
if remaining_budget >= 0:
	 print("You are within your budget.")
else:
	print("You have exceeded your budget.")
total_expense = 0
total_expense = total_expense + user_expense
print("Total expense: " + str(total_expense))	
while total_expense < user_budget:
    new_expense = int(input("Enter the next expense amount"))
    new_category = input("Enter the category for this expense: ")
    new_description = input("Enter the description: ")
    total_expense = total_expense + new_expense
    print("Total expense: " + str(total_expense))
    print("--- New Expense ---")
    print("Category: " + new_category)
    print("Description: " + new_description)
    print("Amount: " + str(new_expense))
    print("Total expense: " + str(total_expense))
    if total_expense >= user_budget:
        break

    choice = input("Do you want to add another expense? (yes/no): ")
    if choice == "no":
    	break
    	
final_remaining = user_budget - total_expense
print("Final remaining budget: " + str(final_remaining))
if final_remaining >= 0:
 	print("You stayed within your budget.")
else:
    print("You exceeded your budget.")