
machines={}
while True:
    machine_number = input("add the number of the machine(or exit): ")

    if machine_number == "exit":
        break

    machine_name = f"machine {machine_number}"

    temperature = float(input("add the temperature of the machine: "))
    machines[machine_name] = temperature

    print(machines)

    print("----machine report----")
    for machine, temp in machines.items():
        print(f"{machine}: {temp}°C")
    if len(machines) > 0:
        avarage = round(sum(machines.values()) / len(machines), 2)
        print(f"avarage temperature: {avarage} °C")