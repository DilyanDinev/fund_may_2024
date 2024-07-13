elements = input().split()

stock = {}

for i in range(0, len(elements), 2):
    key = elements[i]
    value = int(elements[i + 1])
    stock[key] = value

product_for_search = input().split()
for product in product_for_search:
    if product in stock:
        print(f"We have {stock[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")