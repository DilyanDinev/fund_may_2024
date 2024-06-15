def check_employee_happiness(happiness_list, factor_happiness):

    improved_happiness = [employee * factor_happiness for employee in happiness_list]
    average_happiness = sum(improved_happiness) / len(improved_happiness)
    happy_counter = sum(num >= average_happiness for num in improved_happiness)
    total_happiness = len(improved_happiness)

    message = "happy" if happy_counter > total_happiness / 2 else "not happy"
    return f"Score: {happy_counter}/{total_happiness}. Employees are {message}!"



happiness = list(map(int, input().split()))
factor = int(input())
result = check_employee_happiness(happiness, factor)
print(result)