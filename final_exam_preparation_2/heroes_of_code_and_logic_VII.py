def cast_spell(heroes_dict, split_command):
    hero_name, mana_points_needed, spell_name = split_command[1], int(split_command[2]), split_command[3]
    if heroes_dict[hero_name]["MP"] >= mana_points_needed:
        heroes_dict[hero_name]['MP'] -= mana_points_needed
        print(f"{hero_name} has successfully cast {spell_name} and now has {heroes_dict[hero_name]['MP']} MP!")
    else:
        print(f"{hero_name} does not have enough MP to cast {spell_name}!")
    return heroes_dict


def take_damage(heroes_dict, split_command):
    hero_name, damage, attacker = split_command[1], int(split_command[2]), split_command[3]
    heroes_dict[hero_name]['HP'] -= damage
    if heroes_dict[hero_name]['HP'] > 0:
        print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes_dict[hero_name]['HP']} HP left!")
    else:
        print(f"{hero_name} has been killed by {attacker}!")
        del heroes_dict[hero_name]
    return heroes_dict


def recharge(heroes_dict, split_command):
    hero_name, amount = split_command[1], int(split_command[2])
    amount_recovered = amount
    heroes_dict[hero_name]['MP'] += amount
    if heroes_dict[hero_name]['MP'] > 200:
        amount_recovered = amount - (heroes_dict[hero_name]['MP'] - 200)
        heroes_dict[hero_name]['MP'] = 200
    print(f"{hero_name} recharged for {amount_recovered} MP!")
    return heroes_dict



def heal(heroes_dict, split_command):
    hero_name, amount = split_command[1], int(split_command[2])
    amount_recovered = amount
    heroes_dict[hero_name]['HP'] += amount
    if heroes_dict[hero_name]['HP'] > 100:
        amount_recovered = amount - (heroes_dict[hero_name]['HP'] - 100)
        heroes_dict[hero_name]['HP'] = 100
    print(f"{hero_name} healed for {amount_recovered} HP!")
    return heroes_dict


heroes = {}
number_of_heroes = int(input())
for current_hero in range(number_of_heroes):
    hero_name, hit_points, mana_points = input().split()
    heroes[hero_name] = {"HP": int(hit_points), "MP": int(mana_points)}
command = input()
while command != "End":
    command = command.split(" - ")
    action = command[0]
    if action == "CastSpell":
        heroes = cast_spell(heroes, command)
    elif action == "TakeDamage":
        heroes = take_damage(heroes, command)
    elif action == "Recharge":
        heroes = recharge(heroes, command)
    elif action == "Heal":
        heroes = heal(heroes, command)
    command = input()

for hero_name, points in heroes.items():
    print(hero_name)
    print(f"HP: {points['HP']}")
    print(f"MP: {points['MP']}")
