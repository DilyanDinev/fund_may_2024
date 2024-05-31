number = int(input())
word = input()
lst = []
for current_string in range(number):
    some_string = input()
    lst.append(some_string)

filtered_string = []
for string in lst:
    if word in string:
        filtered_string.append(some_string)
print(lst)
print(filtered_string)