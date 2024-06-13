numbers = input().split()
lst = []
for current_number in numbers:
    lst.append(int(current_number))
print(f"The minimum number is {min(lst)}")
print(f"The maximum number is {max(lst)}")
print(f"The sum number is: {sum(lst)}")