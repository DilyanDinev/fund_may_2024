def add_lesson(schedule, lesson_tittle):
    if lesson_tittle not in schedule:
        schedule.append(lesson_tittle)


def insert_lesson(schedule, lesson_tittle, index):
    if lesson_tittle not in schedule:
        schedule.insert(index, lesson_tittle)


def remove_lesson(schedule, lesson_tittle):
    if lesson_tittle in schedule:
        schedule.remove(lesson_tittle)
        exercise_tittle = lesson_tittle + "-Exercise"
        if exercise_tittle in schedule:
            schedule.remove(exercise_tittle)


def swap_lesson(schedule, lesson1, lesson2):
    if lesson1 in schedule and lesson2 in schedule:
        idx1, idx2 = schedule.index(lesson1), schedule.index(lesson2)

        schedule[idx1], schedule[idx2] = schedule[idx2], schedule[idx1]

        exercise1, exercise2 = lesson1 + "-Exercise", lesson2 + "-Exercise"

        if exercise1 in schedule:
            schedule.remove(exercise1)
            schedule.insert(schedule.index(lesson1) + 1, exercise1)

        if exercise2 in schedule:
            schedule.remove(exercise2)
            schedule.insert(schedule.index(lesson2) + 1, exercise2)


def add_exercise(schedule, lesson_tittle):
    exercise_tittle = lesson_tittle + "-Exercise"
    if lesson_tittle in schedule:
        lesson_index = schedule.index(lesson_tittle)
        if exercise_tittle not in schedule:
            schedule.insert(lesson_index + 1, exercise_tittle)
    else:
        schedule.append(lesson_tittle)
        schedule.append(exercise_tittle)


def process_commands(schedule, commands):
    for command in commands:
        parts = command.split(":")
        action = parts[0]

        if action == "Add":
            lesson_tittle = parts[1]
            add_lesson(schedule, lesson_tittle)

        elif action == "Insert":
            lesson_tittle = parts[1]
            index = int(parts[2])
            insert_lesson(schedule, lesson_tittle, index)

        elif action == "Remove":
            lesson_tittle = parts[1]
            remove_lesson(schedule, lesson_tittle)

        elif action == "Swap":
            lesson1 = parts[1]
            lesson2 = parts[2]
            swap_lesson(schedule, lesson1, lesson2)

        elif action == "Exercise":
            lesson_tittle = parts[1]
            add_exercise(schedule, lesson_tittle)

    return schedule


initial_schedule = input().split(", ")
commands = []

while True:
    command = input()
    if command == "course start":
        break

    commands.append(command)


final_schedule = process_commands(initial_schedule, commands)
for index, lesson in enumerate(final_schedule, 1):
    print(f"{index}.{lesson}")