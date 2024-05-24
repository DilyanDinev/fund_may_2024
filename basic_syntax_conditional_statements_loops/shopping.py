budget = int(input())
not_enough_money = False
command = input()
while command != "End":
    spend_money = int(command)
    budget -= spend_money
    if budget < 0:
        not_enough_money = True
        break
    command = input()
if not_enough_money:
    print("You went in overdraft!")
else:
    print("You bought everything needed.")

