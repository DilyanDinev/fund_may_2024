course_dictionary = {}
command = input().split(" : ")
while command[0] != "end":
    course_name, student_name = command[0], command[1]
    if course_name not in course_dictionary.keys():
        course_dictionary[course_name] = []
    course_dictionary[course_name].append(student_name)
    command = input().split(" : ")

for key, value in course_dictionary.items():
    print(f"{key}: {len(value)}")
    for student in value:
        print(f"-- {student}")
