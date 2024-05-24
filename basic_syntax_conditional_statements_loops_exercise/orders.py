number_of_orders = int(input())
total_price = 0

for orders in range(number_of_orders):
    price_order = 0
    price_per_capsule = float(input())
    days = int(input())
    needed_capsules_per_day = int(input())

    if price_per_capsule < 0.01 or price_per_capsule > 100:
        continue
    elif days not in range(1, 31 + 1):
        continue
    elif needed_capsules_per_day not in range(1, 2000 + 1):
        continue

    price_order += price_per_capsule * needed_capsules_per_day * days
    total_price += price_order
    print(f"The price for the coffee is: ${price_order:.2f}")
print(f"Total: ${total_price:.2f}")

