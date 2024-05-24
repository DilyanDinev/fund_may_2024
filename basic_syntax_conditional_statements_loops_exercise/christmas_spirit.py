quantity_of_decoration = int(input())
days = int(input())
spend_money = 0
spirit = 0
for current_day in range(1, days + 1):
    if current_day % 11 == 0:
        quantity_of_decoration += 2
    if current_day % 2 == 0:
        spend_money += 2 * quantity_of_decoration
        spirit += 5
    if current_day % 3 == 0:
        spend_money += (5 + 3) * quantity_of_decoration
        spirit += 3 + 10
    if current_day % 5 == 0:
        spend_money += 15 * quantity_of_decoration
        spirit += 17
    if current_day % 10 == 0:
        spirit -= 20
        spend_money += 23
    if current_day % 3 == 0 and current_day % 5 == 0:
        spirit += 30
if days % 10 == 0:
    spirit -= 30
print(f"Total cost: {spend_money}")
print(f"Total spirit: {spirit}")




