words = input().split()
dictionary = {}

for word in words:
    word_lower = word.lower()
    if word_lower not in dictionary:
        dictionary[word_lower] = 0
    dictionary[word_lower] += 1

for word_lower, current_word in dictionary.items():
    if current_word % 2 != 0:
        print(word_lower, end=" ")