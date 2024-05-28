number = int(input())
total_water = 0
for liters in range(number):
    current_liters = int(input())
    if current_liters + total_water > 255:
        print("Insufficient capacity!")
        continue
    total_water += current_liters

print(total_water)