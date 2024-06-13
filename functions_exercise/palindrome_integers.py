# numbers = input().split(", ")
#
# for current_num in numbers:
#     list_numbers = []
#     for i in current_num:
#         list_numbers.append(i)
#     if list_numbers[0] == list_numbers[-1]:
#         print(True)
#     else:
#         print(False)

# def palindrome(nums):
#     for number in nums:
#         is_palindrome = number[0] == number[-1]
#         print(is_palindrome)
#
#
# numbers = input().split(", ")
# palindrome(numbers)


# lst = input().split(", ")
#
# for i, number in enumerate(lst):
#     length = len(number) // 2
#     left_side = number[:length]
#     right_side = number[:: -1]
#     new_side = right_side[:length]
#     if left_side == new_side:
#         print(True)
#     else:
#         print(False)

def is_palindrome(some_number_as_string):
    return some_number_as_string == some_number_as_string[::-1]


number_as_string = input().split(", ")
for number in number_as_string:
    print(is_palindrome(number))