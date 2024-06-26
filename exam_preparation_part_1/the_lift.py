waiting_people = int(input())
current_state_of_the_lift = [int(integer) for integer in input().split()]
number_of_wagons = 0
flag = False
for i, wagon in enumerate(current_state_of_the_lift):
    if waiting_people > 3:
        diff = 4 - int(wagon)
        waiting_people -= diff
        current_state_of_the_lift[i] += diff
        number_of_wagons += 1
    else:
        current_state_of_the_lift[i] += waiting_people
        waiting_people -= waiting_people
        if current_state_of_the_lift[i] == 4:
            number_of_wagons += 1
    if number_of_wagons == len(current_state_of_the_lift):
        flag = True

if waiting_people > 0:
    print(f"There isn't enough space! {waiting_people} people in a queue!")
elif not flag:
    print("The lift has empty spots!")

print(*current_state_of_the_lift, sep=" ")


