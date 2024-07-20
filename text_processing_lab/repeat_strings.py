strings = input().split()
list_string = [text * len(text) for text in strings]
print("".join(list_string))