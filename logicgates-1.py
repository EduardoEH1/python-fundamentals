while True:
    gate = input("Select (AND/OR/NOT/XOR/NAND/NOR/XNOR): ")

    a = input ("A= ")
    if gate != "NOT":
        b = input ("B= ")
    if gate == "NOT":
        if a =="1":
            result = 0
        else:
            result = 1


    elif gate =="AND":
        if a == "1" and b == "1":
            result = 1
        else:
            result = 0

    elif gate =="OR":
        if a == "1" or b =="1":
            result = 1
        else:
            result = 0

    elif gate =="XOR":
        if a != b:
            result = 1
        else:
            result = 0

    elif gate =="XNOR":
        if a != b:
            result = 0
        else:
            result = 1

    elif gate == "NAND":
        if a== "1" and b =="1":
            result = 0
        else:
            result = 1

    elif gate =="NOR":
        if a == "1" or b =="1":
            result = 0
        else:
            result = 1

    print(f"result: {result}")
    