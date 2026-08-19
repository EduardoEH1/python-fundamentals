def add_contact(name, number):
    file = open("contacts.txt", "a")
    file.write(name + " - " + number + "\n")
    file.close()

def show_contacts():
    try:
        file = open("contacts.txt" , "r")
        content = file.read()
        print("contacts list")
        print(content)
        file.close()
    except FileNotFoundError:
        print("\n no contacts found. Try add one first")


while True:

    opcion = input("choose: add / show / exit : ")

    if opcion == "add":
        while True:
            number = input("add number: ")
            if number.isdigit():
                break
            else:
                print("ERROR!: Please enter a valid number(digits only). TRY AGAIN")

        name = input("add name: ")
        add_contact(name, number)
        print("contact added: " + name + " - " + number)

    elif opcion == "show":
        show_contacts()
    
    elif opcion == "exit":
        print("exit program")
        break

    else:
        print("invalid opcion")

