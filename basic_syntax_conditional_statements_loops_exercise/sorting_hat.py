student_name = input()
problem = False
while student_name != "Welcome!":
    if student_name == "Voldemort":
        problem = True
        break
    if len(student_name) < 5:
        print(f"{student_name} goes to Gryffindor.")
    elif len(student_name) == 5:
        print(f"{student_name} goes to Slytherin.")
    elif len(student_name) == 6:
        print(f"{student_name} goes to Ravenclaw.")
    elif len(student_name) > 6:
        print(f"{student_name} goes to Hufflepuff.")
    student_name = input()
if problem:
    print("You must not speak of that name!")
else:
    print("Welcome to Hogwarts.")
