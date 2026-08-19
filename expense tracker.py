def add_expense(date, type, category, amaunt):
    file = open("expense.txt", "a")
    file.write(date + "-" + type + "-" + category + "-" + amaunt + "\n")
    file.close()

def show_expense():
    try:
        file = open("expense.txt", "r")
        content = file.read()
        print("EXPENSE LIST")
        print(content)
        file.close()
    except FileNotFoundError:
        print("\n expense not found ")

def total_expense():
    try:
        file = open("expense.txt", "r")
        lines = file.readlines()
        file.close()

        total = 0
        for line in lines:
            datos = line.split("-")
            monto = datos[3].strip()
            total = total + int(monto)

        print("TOTAL EXPENSE:")
        print(total)
    except FileNotFoundError:
        print("\n expense not found ")
    

while True:
    
    option = input("choose: add / show / total (expense):  ")
    if option == "add":
    
        month = input("add month: ")
        day = input("add day: ")
        year = input("add year: ")
        date = month + "/" + day + "/" + year

        while True:
            type_option = input("choose the number (1) for fixed, or (2) for variable expense: ")
            if type_option == "1":
                exp_type = "fixed"
                break
            elif type_option == "2":
                exp_type = "variable"
                break
            else:
                print("invalid option, select 1 or 2")
            
        category = input("enter the category (rent,food, netflix, etc): ")
        amaunt = input("enter the amaunt of the expense: ")
        add_expense(date, exp_type, category, amaunt)
        print("expense saved!!")

    if option == "show":
        show_expense()

    if option == "total":
        total_expense()