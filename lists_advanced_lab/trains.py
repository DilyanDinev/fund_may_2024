wagons = [0] * int(input())

while True:
    command = input().split()
    if command[0] == "End":
        print(wagons)
        break
    elif command[0] == "add":
        wagons[-1] += int(command[1])
    elif command[0] == "insert":
        i = int(command[1])
        people = int(command[2])
        wagons[i] += people
    elif command[0] == "leave":
        i = int(command[1])
        people = int(command[2])
        wagons[i] -= people
