def order(product, number):
    if product == "coffee":
        return number * 1.5
    elif product == "water":
        return number * 1
    elif product == "coke":
        return number * 1.4
    elif product == "snacks":
        return number * 2


current_product = input()
current_number = float(input())
result = order(current_product, current_number)
print(f"{result:.2f}")