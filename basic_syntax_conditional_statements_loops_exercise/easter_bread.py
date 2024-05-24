budget = float(input())
flour_price_per_kilo = float(input())

eggs_price_per_packet = flour_price_per_kilo * 0.75
liter_milk_price = flour_price_per_kilo * 1.25
recipe_price = flour_price_per_kilo + eggs_price_per_packet + (liter_milk_price / 4)

number_of_loaves = 0
number_of_colored_eggs = 0
not_enough_money = False

while budget > 0:

    if budget < recipe_price:
        not_enough_money = True
        break
    number_of_loaves += 1
    number_of_colored_eggs += 3
    budget -= recipe_price

    if number_of_loaves % 3 == 0:
        number_of_colored_eggs -= (number_of_loaves - 2)

if not_enough_money:
    print(f"You made {number_of_loaves} loaves of Easter bread! Now you have {number_of_colored_eggs} eggs and {budget:.2f}BGN left.")




