first_index = int(input())
last_index = int(input())
for i in range(first_index, last_index + 1):
    if i == last_index:
        print(chr(last_index))
    else:
        print(chr(i), end=" ")