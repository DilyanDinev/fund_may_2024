list_of_cards = input().split(", ")
number_of_commands = int(input())

for i in range(number_of_commands):
    current_command = input().split(", ")
    command = current_command[0]

    if command == "Add":
        card_name = current_command[1]
        if card_name not in list_of_cards:
            list_of_cards.append(card_name)
            print("Card successfully added")
        else:
            print("Card is already in the deck")

    elif command == "Remove":
        card_name = current_command[1]
        if card_name in list_of_cards:
            list_of_cards.remove(card_name)
            print("Card successfully removed")
        else:
            print("Card not found")

    elif command == "Remove At":
        index = current_command[1]
        if int(index) in range(len(list_of_cards)):
            del list_of_cards[int(index)]
            print("Card successfully removed")
        else:
            print("Index out of range")

    elif command == "Insert":
        index = int(current_command[1])
        card_name = current_command[2]
        if index not in range(len(list_of_cards)):
            print("Index out of range")
        else:
            if card_name not in list_of_cards:
                list_of_cards.insert(index, card_name)
                print("Card successfully added")
            else:
                print("Card is already added")

print(*list_of_cards, sep=", ")