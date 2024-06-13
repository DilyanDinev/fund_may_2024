def sort_nums(nums):
    list_numbers = []
    for current_number in nums:
        list_numbers.append(int(current_number))
    sorted_numbers = sorted(list_numbers)
    return sorted_numbers


numbers = input().split()
print(sort_nums(numbers))

# numbers = input().split()
# list_numbers = []
# for current_number in numbers:
#     list_numbers.append(int(current_number))
# sorted_numbers = sorted(list_numbers)
# print(sorted_numbers)