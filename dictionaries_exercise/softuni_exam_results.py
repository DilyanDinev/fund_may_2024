users_point_dictionary = {}
courses_dictionary = {}
while True:
    current_result = input().split("-")
    if len(current_result) == 1:
        break
    elif len(current_result) == 2:
        name = current_result[0]
        del users_point_dictionary[name]
    else:
        name, course, points = current_result[0], current_result[1], int(current_result[2])
        if name not in users_point_dictionary.keys():
            users_point_dictionary[name] = 0
        if users_point_dictionary[name] < points:
            users_point_dictionary[name] = points
        if course not in courses_dictionary.keys():
            courses_dictionary[course] = 0
        courses_dictionary[course] += 1
print("Results:")
for name, max_points in users_point_dictionary.items():
    print(f"{name} | {max_points}")
print("Submissions:")
for course, number_of_students in courses_dictionary.items():
    print(f"{course} - {number_of_students}")