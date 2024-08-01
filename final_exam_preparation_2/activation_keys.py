def contains(activation_key, some_command):
    substring = some_command[1]
    if substring in activation_key:
        return f"{activation_key} contains {substring}"
    return "Substring not found!"


def flip(activation_key, some_command):
    upper_lower = some_command[1]
    start_index = int(some_command[2])
    end_index = int(some_command[3])
    before_string = activation_key[:start_index]
    after_string = activation_key[end_index:]
    if upper_lower == "Upper":
        substring = activation_key[start_index: end_index].upper()
        activation_key = before_string + substring + after_string
    elif upper_lower == "Lower":
        substring = activation_key[start_index: end_index].lower()
        activation_key = before_string + substring + after_string
    return activation_key


def slice(activation_key, some_command):
    start_index = int(some_command[1])
    end_index = int(some_command[2])
    before_string = activation_key[:start_index]
    after_string = activation_key[end_index:]
    activation_key = before_string + after_string
    return activation_key


raw_activation_key = input()
command = input()
while command != "Generate":
    command = command.split(">>>")
    action = command[0]
    if action == "Contains":
        print(contains(raw_activation_key, command))
    elif action == "Flip":
        raw_activation_key = flip(raw_activation_key, command)
        print(raw_activation_key)
    elif action == "Slice":
        raw_activation_key = slice(raw_activation_key, command)
        print(raw_activation_key)
    command = input()
print(f"Your activation key is: {raw_activation_key}")