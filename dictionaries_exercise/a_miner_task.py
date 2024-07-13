dictionary = {}
while True:
    command = input()
    if command == "stop":
        break
    current_quantity = int(input())
    if command not in dictionary:
        dictionary[command] = 0
    dictionary[command] += current_quantity

for recourse, quantity in dictionary.items():
    print(f"{recourse} -> {quantity}")

