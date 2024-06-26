first_employee_efficiency = int(input())
second_employee_efficiency = int(input())
third_employee_efficiency = int(input())
number_of_students = int(input())
total_efficiency = first_employee_efficiency + second_employee_efficiency + third_employee_efficiency
total_time = 0

while number_of_students > 0:
    total_time += 1
    if total_time % 4 == 0:
        continue
    number_of_students -= total_efficiency

print(f"Time needed: {total_time}h.")
