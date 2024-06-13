def even_numbers(some_numbers):
    list_numbers = []
    for current_number in some_numbers:
        if int(current_number) % 2 == 0:
            list_numbers.append(int(current_number))
    return list_numbers


numbers = input().split()
print(even_numbers(numbers))

# def even_nums(nums):
#     return nums % 2 == 0
#
#
# number = input().split()
# num_as_integer = []
# for num in number:
#     num_as_integer.append(int(num))
# final_list = list(filter(even_nums, num_as_integer))
# print(final_list)