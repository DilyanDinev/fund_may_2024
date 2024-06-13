def characters(first_symbol, second_symbol):
    lst_char = []
    for char_as_digit in range(ord(first_symbol) + 1, ord(second_symbol)):
        lst_char.append(chr(char_as_digit))
    return lst_char


first_character = input()
second_character = input()
final_characters = characters(first_character, second_character)
print(" ".join(final_characters))