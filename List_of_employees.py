import uuid

employees = []

for i in range(1, 11):
    name = input("Enter name for employee {}: ".format(i))

    employee = {
        'id': str(uuid.uuid4()),
        'name': name
    }

    employees.append([employee])

print("Employee list:")
for employee_list in employees:
    for employee in employee_list:
        print(employee)