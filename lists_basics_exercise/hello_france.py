items = input().split("|")
budget = float(input())
current_budget = budget
ticket_price = 150
profit = 0
prices = []

for i in items:
    arg = i.split("->")
    current_item = arg[0]
    current_sum = float(arg[1])
    item_is_valid = False

    if current_item == "Clothes" and current_sum <= 50:
        item_is_valid = True
    elif current_item == "Shoes" and current_sum <= 35:
        item_is_valid = True
    elif current_item == "Accessories" and current_sum <= 20.5:
        item_is_valid = True

    if item_is_valid:
        if current_sum <= current_budget:
            current_budget -= current_sum
            current_price = current_sum * 1.4
            profit += current_price - current_sum
            prices.append(f"{current_price:.2f}")

budget += profit
print(*prices)

print(f"Profit: {profit:.2f}")

if budget >= ticket_price:
    print("Hello, France!")
else:
    print("Not enough money.")