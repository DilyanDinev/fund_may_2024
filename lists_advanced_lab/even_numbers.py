def even_index(nums):
    lst = [index for index, digit in enumerate(nums) if digit % 2 == 0]
    return lst


numbers = list(map(int, input().split(", ")))
print(even_index(numbers))