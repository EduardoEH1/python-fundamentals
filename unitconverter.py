
def cel_to_fah(celsius):
    result = (celsius * 9/5) + 32
    return result
def fah_to_cel(fahrenheit):
    result = (fahrenheit - 32) * 5/9
    return result
def mi_to_km(miles):
    result = miles * 1.60934
    return result
def km_to_mi(km): 
    result = km / 1.60934
    return result
def cm_to_m(cm):
    result = cm / 100
    return result
def m_to_cm(m):
    result = m * 100
    return result

print("(1) celsius to fahrenheit")
print("(2) fahrenheit to celsius")
print("(3) miles to kilometers")
print(("(4)kilometers to miles"))
print("(5)cm to m")
print("(6)m to cm")

while True:
    option = input("choose one option between 1-6: ")
    if option == "1":
        celsius = float(input("add value on celsius: "))
        result = cel_to_fah(celsius)
        print(f"{result}")
    elif option == "2":
        fahrenheit = float(input("add values on fahrenheit: "))
        result = fah_to_cel(fahrenheit)
        print(f"{result}")
    elif option == "3":
        miles = float(input("add value on miles: "))
        result = mi_to_km(miles)
        print(f"{result}")
    elif option == "4":
        km = float(input("add value on kilometers: "))
        result = km_to_mi(km)
        print(f"{result}")
    elif option == "5":
        cm = float(input("add value on centimeters: "))
        result = cm_to_m(cm)
        print(f"{result}")
    elif option == "6":
        m = float(input("add value on meters: "))
        result = m_to_cm(m)
        print(f"{result}")
    else:
        print("ERROR")
 