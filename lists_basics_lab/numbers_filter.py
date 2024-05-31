number = int(input())
lst = []

for _ in range(number):
    current_num = int(input())
    lst.append(current_num)
command = input()
filtered_num = []
if command == "even":
    for num in lst:
        if num % 2 == 0:
            filtered_num.append(num)
elif command == "odd":
    for num in lst:
        if num % 2 != 0:
            filtered_num.append(num)
elif command == "negative":
    for num in lst:
        if num < 0:
            filtered_num.append(num)
elif command == "positive":
    for num in lst:
        if num >= 0:
            filtered_num.append(num)
print(filtered_num)