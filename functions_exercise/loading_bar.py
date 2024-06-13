def loading_bar(num):
    if num == 100:
        return f"100% Complete!\n[%%%%%%%%%%]"
    else:
        some_digit = num // 10
        return f"{num}% [{'%' * some_digit}{'.' * (10 - some_digit)}]\nStill loading..."


number = int(input())
print(loading_bar(number))