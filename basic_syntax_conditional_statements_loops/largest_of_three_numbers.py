# number = int(input())
# second_number = int(input())
# third_number = int(input())
#
# if number > second_number and number > third_number:
#     print(number)
# elif second_number > number and second_number > third_number:
#     print(second_number)
# else:
#     print(third_number)

num1, num2, num3 = int(input()), int(input()), int(input())
largest = max(num1, num2, num3)
print(largest)