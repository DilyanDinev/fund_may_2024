numbers_as_string = input().split()
lst = []
for rounded_num in numbers_as_string:
    number = float(rounded_num)
    current_number = round(number)
    lst.append(current_number)
print(lst, sep=" ")
