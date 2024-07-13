text = [character for character in input() if character != " "]
dictionary = {}
for character in text:
    if character not in dictionary.keys():
        dictionary[character] = 0
    dictionary[character] += 1

for symbol, occurrences in dictionary.items():
    print(f"{symbol} -> {occurrences}")
