numbers_str = input().split()
remover = int(input())
numbers = []
for num in numbers_str:
    numbers.append(int(num))

for _ in range(remover):
    numbers.remove(min(numbers))

print(*numbers, sep=", ")