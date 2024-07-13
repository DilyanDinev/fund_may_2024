dictionary = {}
count = int(input())

for _ in range(count):
    student_name = input()
    current_grade = float(input())
    if student_name not in dictionary:
        dictionary[student_name] = []
    dictionary[student_name].append(current_grade)

for key, value in dictionary.items():
    total_grade = sum(value) / len(value)
    if total_grade >= 4.50:
        print(f"{key} -> {total_grade:.2f}")