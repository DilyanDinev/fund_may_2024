cards = input().split()
number_of_shuffle = int(input())
for shuffle in range(number_of_shuffle):
    middle_of_dec = len(cards) // 2
    left_part = cards[:middle_of_dec]
    right_part = cards[middle_of_dec:]
    dec_after_shuffling = []
    for card_index in range(len(left_part)):
        dec_after_shuffling.append(left_part[card_index])
        dec_after_shuffling.append(right_part[card_index])
    cards = dec_after_shuffling
print(cards)