numbers = input().split()

absolute_value = []

for num in numbers:
    absolute_value.append(abs(float(num)))

print(absolute_value)