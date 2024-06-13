def factorial_division(num1, num2):
    num = 1
    number = 1
    for current_num in range(1, num1 + 1):
        num *= current_num
    for current_num in range(1, num2 + 1):
        number *= current_num
    result = num // number
    return f"{result:.2f}"


first_number = int(input())
second_number = int(input())
print(factorial_division(first_number, second_number))