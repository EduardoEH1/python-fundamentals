

fruits = {
    "apple": 2.20,
    "watermelon": 0.90,
    "banana": 1.10,
    "orange": 1.50,
    "mango": 2.80,
    "strawberries": 1.80,
    "grapes": 2,
    "kiwi": 1.20,

}

while True:
    name_fruit = input("What fruit do you want?: ")

    if name_fruit in fruits:
        print(name_fruit)
        try:
            measure = float(input("Insert the Kilograms: "))
            price = fruits[name_fruit]
            total = round(price * measure,2)
            print(f"Total: {total} dollars")
        except:
            print("error")
    else:
        print("Sorry we don't have that fruit")

    continue_shopping = input("Do you want to buy another fruit (yes/no): ")
    if continue_shopping == "no":
        break
    else:
        print("continuing shopping")

