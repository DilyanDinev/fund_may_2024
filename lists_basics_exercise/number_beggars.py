money_as_string = input().split(", ")
number_of_beggars = int(input())
money_as_integer = []
for money in money_as_string:
    money_as_integer.append(int(money))
final_money = []
start_index = 0
for current_beggar in range(number_of_beggars):
    current_beggar_sum = 0
    for current_money in range(start_index, len(money_as_integer), number_of_beggars):
        current_beggar_sum += money_as_integer[current_money]
    start_index += 1
    final_money.append(current_beggar_sum)
print(final_money)