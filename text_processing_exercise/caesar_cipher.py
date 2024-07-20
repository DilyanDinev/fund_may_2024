text = input()
for i in text:
    encrypted = ord(i) + 3
    print(chr(encrypted), end="")