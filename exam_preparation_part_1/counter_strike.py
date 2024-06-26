# energy = int(input())
# command = input()
# won_battles = 0
# flag = False
# while command != "End of battle":
#     needed_energy_to_reach = int(command)
#     if energy >= needed_energy_to_reach:
#         energy -= needed_energy_to_reach
#         won_battles += 1
#     else:
#         flag = True
#         break
#     if won_battles % 3 == 0:
#         energy += won_battles
#     command = input()
#
# if flag:
#     print(f"Not enough energy! Game ends with {won_battles} won battles and {energy} energy")
# else:
#     print(f"Won battles: {won_battles}. Energy left: {energy}")

def battle_game(energy):
    won_battles = 0
    command = input()
    flag = False
    while command != "End of battle":
        needed_energy_to_reach = int(command)
        if energy >= needed_energy_to_reach:
            energy -= needed_energy_to_reach
            won_battles += 1
        else:
            flag = True
            break
        if won_battles % 3 == 0:
            energy += won_battles
        command = input()
    if flag:
        return f"Not enough energy! Game ends with {won_battles} won battles and {energy} energy"
    else:
        return f"Won battles: {won_battles}. Energy left: {energy}"


initial_energy = int(input())
result = battle_game(initial_energy)
print(result)