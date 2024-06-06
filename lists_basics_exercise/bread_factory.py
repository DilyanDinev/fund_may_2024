working_day_events = input().split("|")
current_energy = 100
coins = 100
flag = True
for i in working_day_events:
    agr = i.split("-")
    event_or_ingredient = agr[0]
    number = int(agr[1])

    if event_or_ingredient == "rest":
        energy = current_energy
        current_energy += number
        if current_energy > 100:
            current_energy = 100
        gained = current_energy - energy
        print(f"You gained {gained} energy.")
        print(f"Current energy: {current_energy}.")

    elif event_or_ingredient == "order":
        if current_energy >= 30:
            coins += number
            current_energy -= 30
            print(f"You earned {number} coins.")
        else:
            current_energy += 50
            print("You had to rest!")

    else:
        if coins >= number:
            coins -= number
            print(f"You bought {event_or_ingredient}.")
        else:
            flag = False
            break
if flag:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {current_energy}")
else:
    print(f"Closed! Cannot afford {event_or_ingredient}.")
