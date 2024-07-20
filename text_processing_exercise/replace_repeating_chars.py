some_string = input()
final_string = ""
last_string = ""
for current_string in some_string:
    if current_string != last_string:
        final_string += current_string
        last_string = current_string
print(final_string)
