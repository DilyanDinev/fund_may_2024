def odd_even_digits(num):
    odd_sum = 0
    even_sum = 0
    for current_digit in num:
        digit_as_integer = int(current_digit)
        if digit_as_integer % 2 == 0:
            even_sum += digit_as_integer
        else:
            odd_sum += digit_as_integer
    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"


number = input()
print(odd_even_digits(number))