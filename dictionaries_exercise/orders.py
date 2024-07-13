products_dictionary = {}

while True:
    command = input().split()
    if command[0] == "buy":
        break
    else:
        product, price, quantity = command[0], float(command[1]), int(command[2])

    if product not in products_dictionary.keys():
        products_dictionary[product] = [price, quantity]
    else:
        products_dictionary[product][0] = price
        products_dictionary[product][1] += quantity

for key, value in products_dictionary.items():
    total_price = value[0] * value[1]
    print(f"{key} -> {total_price:.2f}")
