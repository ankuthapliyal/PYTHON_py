# Expencse Tracker Project

expensesList = [] #list of all expenses in form od dictionary

print("Welcome to Expense Tracker :...Khrcha Kam Kiya karo..😁")

while True:
    print("\n=====MENU=====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Amount")
    print("4. Exit")

    choice = int(input("Please Enter Your Choice : "))
    # ADD Expenses

    if(choice == 1):
        date = input("Enter Date (DD/MM/YYYY) : ")
        category = input("Enter the Category ? (Food, Travel, Shoping, Books, Moveshow) : ")
        descreption = input("Enter All Detail : ")
        amount = float(input("Enter the Amount : "))

        expense = {
            "date": date,
            "category": category,
            "description": descreption,
            "amount": amount
        }
        expensesList.append(expense)
        print("\n Expenses added Succesfully")

# 2 View All Expenses
    elif(choice == 2):
        if(len(expensesList) == 0):
            print("No Expenses Added Yet Give the Amount Spended...")
        else:
            print("\n=======This is Your Expense======")

            count = 1

            for i in expensesList:
                print(f"Expense {count} -> "f"Date: {i['date']}, "f"Category: {i['category']}, "f"Description: {i['description']}, "f"Amount: ₹{i['amount']}")
                count = count + 1

# View Total Expenses
    elif(choice == 3):
       
       total = 0

       for i in expensesList:
           total = total + i["amount"]
        
       print("\n TOTAL EPENSES COST = ₹",total)

# 4 Exit
    elif(choice == 4):
        print("Thankyou for Using Our System.🙏....")
        break

    else:
        print("Invalid Choice ...❌ Plese Try Agin")