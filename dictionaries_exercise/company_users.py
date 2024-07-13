dictionary = {}

while True:
    command = input().split(" -> ")
    if command[0] == "End":
        break
    else:
        name_of_company, employee_id = command[0], command[1]
        if name_of_company not in dictionary.keys():
            dictionary[name_of_company] = []
        if employee_id not in dictionary[name_of_company]:
            dictionary[name_of_company].append(employee_id)

for company_name in dictionary.keys():
    print(company_name)
    for employee in dictionary[company_name]:
        print(f"-- {employee}")
