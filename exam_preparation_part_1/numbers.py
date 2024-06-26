numbers = [int(num) for num in input().split()]
average_value = sum(numbers) / len(numbers)
current_list = [num for num in numbers if num > average_value]
if current_list:
    result = sorted(current_list, reverse=True)[:5]
    print(*result)
else:
    print("No")




