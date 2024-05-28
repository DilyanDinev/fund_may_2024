number_of_symbols = int(input())
total_sum = 0
for ascii_char in range(number_of_symbols):
    current_char = input()
    total_sum += ord(current_char)
print(f"The sum equals: {total_sum}")