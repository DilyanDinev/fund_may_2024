def perfect_number(number: int) -> str:
    numbers_box = 0
    for current_number in range(1, number):
        if number % current_number == 0:
            numbers_box += current_number
    if numbers_box == number:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


nums = int(input())
print(perfect_number(nums))