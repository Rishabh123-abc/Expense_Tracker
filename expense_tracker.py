#Expense Tracker app
expenses = []
while(True):
    print('1.Add Expenses \
    2.View Expenses \
    3.Total Expenses  \
    4.Delete Expenses \
    5.Max Expense \
    6.Min Expenses  \
    7.Exit')
    choice = int(input('Enter your choice'))
    if choice == 1:
        item = input('Enter the name of the item')
        amount = float(input('Enter the amount of item'))
        expenses.append([item,amount])
        print('Expenses added successfully')
    elif choice == 2:
        if not expenses:
            print('Nothing in your expenses')
        else:
            for item in expenses:
                print(f'Item {item[0]}:Value {item[1]}')
    elif choice == 3:
        if not expenses:
            print('Nothing you done in expenses')
        else:
            total = 0
            for item in expenses:
                total += item[1]
            print(f'Total expenses is {total}')
    elif choice == 4:
        item = input('Enter the name of expense you want to delete')
        found = False
        for expense in expenses:
            if expense[0].lower() == item.lower():
                expenses.remove(expense)
                found = True
                print('Expense Deleted Successfully')
                break
            if not found:
                print('Item not found in expenses')
    elif choice == 5:
        if not expenses:
            print('Nothing you done in expenses')
        else:
            highest = max(expenses,key = lambda x:x[1])
            print(f'Highest Expense:{highest[0]}')
            print(f'Highest Expense:{highest[1]}')
    elif choice == 6:
            if not expenses:
                print('Nothing you done in expenses')
            else:
                highest = min(expenses,key = lambda x:x[1])
                print(f'Highest Expense:{highest[0]}')
                print(f'Highest Expense:{highest[1]}')
    elif choice == 7:
        print('Bye')
        break
    else:
        print('Invalid input')