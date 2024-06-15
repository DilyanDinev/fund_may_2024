text = input()
final_text = [letter for letter in text if letter.lower() not in ['a', 'o', 'u', 'e', 'i']]
print("".join(final_text))