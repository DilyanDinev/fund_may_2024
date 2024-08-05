travel_rout = input().split("||")
fuel = int(input())
ammunition = int(input())

for current_command in travel_rout:
    command = current_command.split()
    if command[0] == "Titan":
        print("You have reached Titan, all passengers are safe.")
        break
    else:
        action, number = command[0], int(command[1])
        if action == "Travel":
            if fuel >= number:
                fuel -= number
                print(f"The spaceship travelled {number} light-years.")
            else:
                print("Mission failed.")
                break

        elif action == "Enemy":
            if ammunition >= number:
                ammunition -= number
                print(f"An enemy with {number} armour is defeated.")
            else:
                fuel -= number * 2
                if fuel >= 0:
                    print(f"An enemy with {number} armour is outmaneuvered.")
                else:
                    print("Mission failed.")
                    break

        elif action == "Repair":
            fuel += number
            ammunition += number * 2
            print(f"Ammunitions added: {number * 2}.")
            print(f"Fuel added: {number}.")
