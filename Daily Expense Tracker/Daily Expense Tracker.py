expenses=[]
while True:
    print("=====Welcome to the Daily Expense Tracker!=====\n")
    print("Menu:")
    print("1. Add a new expense")
    print("2. View all expenses")
    print("3. Calculate total and average expense")
    print("4. Clear all expenses")
    print("5. Exit")
    choice=int(input("Enter Choice: "))
    match choice:
        case 1:
            inp=float(input("Enter amount: "))
            expenses.append(inp)
            print("Expense added successfully!")
        case 2:
            if expenses:
                print("Your expenses:")
                for i in range(len(expenses)):
                    print(f"{i+1}. {expenses[i]}")
            else:
                print("No expenses recorded yet.")
        case 3:
            if expenses:
                total=0.0
                for exp in expenses:
                    total+=exp
                print("Total expense:",total)
                avg=total/len(expenses)
                print("Average expense:",avg)
            else:
                print("No expenses recorded yet.")
        case 4:
            expenses=[]
            print("All expenses cleared.")   
        case 5:
            print("Exiting the Daily Expense Tracker. Goodbye!")
            break
        case _:
            print("Invalid choice. Please try again.")
