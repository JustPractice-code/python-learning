#expense tracker app logic
expenses = []
category = []
dates = []
while True:
    print("\nChoose option as appropriate option")
    print("Entering new expense : 'N'")
    print("View all Expenses : 'V'")
    print("Want total amount spended : 'T'")
    print("View expense of any particular category : 'VP'")
    print("Exit : 'X'")
    choice = input("Enter your choice : ")
    if choice.upper() == 'N':
        exp = int(input("Enter amount : "))
        cat = input("Enter category : ")
        date = input("Enter date of spend (dd-mm-yy): ")    
        expenses.append(exp)
        category.append(cat)
        dates.append(date)
    elif choice.upper() == 'T':
        if len(expenses) == 0:
            print("You not spend any money")
        else:
            total = 0
            for i in expenses:
                total += i
            print(f"Your total spending amount is {total}")
    elif choice.upper() == 'V':
        if len(expenses) == 0:
            print("You Don't have any expense to be shown")
        else:
            a = 0
            while a < len(expenses):
                print(f"You spend Rupees {expenses[a]} on {category[a]} on {dates[a]}.")
                a += 1
    elif choice.upper() == 'VP':
        cate = input("Enter the name of category : ")
        if cate in category:
            a = category.index(cate)
            b = category.count(cate)
            c = len(category) - 1
            if b > 1:
                temp = 0
                for i in range(c):
                    d = category.index(cate,temp)
                    print(f"You spend Rupees {expenses[d]} on {category[d]} on {dates[d]}.")
                    temp = d + 1
            else:
                print(f"You spend Rupees {expenses[a]} on {category[a]} on {dates[a]}.")
    elif choice.upper() == 'X':
        break
    else:
        print("You entered wrong input")