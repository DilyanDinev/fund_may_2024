number_of_cities = int(input())
total_profit = 0

for current_city in range(1, number_of_cities + 1):
    name_of_city = input()
    earned_money = float(input())
    expenses = float(input())
    if current_city % 3 == 0 and current_city % 5 == 0:
        earned_money *= 0.9
    elif current_city % 3 == 0:
        expenses += expenses * 0.5
    elif current_city % 5 == 0:
        earned_money *= 0.9

    current_profit = earned_money - expenses
    total_profit += current_profit
    print(f"In {name_of_city} Burger Bus earned {current_profit:.2f} leva.")

print(f"Burger Bus total profit: {total_profit:.2f} leva.")