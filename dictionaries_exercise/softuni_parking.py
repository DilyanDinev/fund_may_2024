parking = {}
number_of_commands = int(input())
for command in range(number_of_commands):
    current_command = input().split()
    if current_command[0] == "register":
        user_name, license_plate_number = current_command[1], current_command[2]
        if user_name in parking.keys(): # ако името на шофьора е в регистъра
            print(f"ERROR: already registered with plate number {license_plate_number}")
        else: # ако не е
            parking[user_name] = license_plate_number
            print(f"{user_name} registered {license_plate_number} successfully")
    elif current_command[0] == "unregister":
        user_name = current_command[1]
        if user_name not in parking.keys():
            print(f"ERROR: user {user_name} not found")
        else:
            del parking[user_name]
            print(f"{user_name} unregistered successfully")

for username, license_plate_number in parking.items():
    print(f"{username} => {license_plate_number}")
