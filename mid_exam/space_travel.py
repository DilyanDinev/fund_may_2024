sequence = input().split("||")
fuel = int(input())
ammunition = int(input())
flag = False
for current_travel in sequence:
    travel = current_travel.split()
    current_command = str(travel[0])
    if len(agr) > 1:
        some_numbers = int(travel[1])
    if current_command == "Travel":
        if fuel >= some_numbers:
            fuel -= some_numbers
            print(f"The spaceship travelled {some_numbers} light-years.")
        else:
            print("Mission failed.")
            break
    elif current_command == "Enemy":
        if ammunition >= some_numbers:
            ammunition -= some_numbers
            print(f"An enemy with {some_numbers} armour is defeated.")
        else:
            fuel -= some_numbers * 2
            if fuel >= 0:
                print(f"An enemy with {some_numbers} armour is outmaneuvered.")
            else:
                print("Mission failed.")
                break
    elif current_command == "Repair":
        fuel += some_numbers
        added_ammunition = some_numbers * 2
        ammunition = added_ammunition
        print(f"Ammunitions added: {added_ammunition}.")
        print(f"Fuel added: {some_numbers}.")
    elif current_command == "Titan":
        flag = True
        break
if flag:
    print("You have reached Titan, all passengers are safe.")