employees = []

while True:
    employee_data = {}

    name = input("Enter employee name (or 'quit' to exit): ")
    if name.lower() == 'quit':
        break

    employee_data['name'] = name

    employee_id = input("Enter employee ID: ")
    if employee_id:
        employee_data['id'] = employee_id
    else:
        employee_data['id'] = str(len(employees) + 1)

    employees.append(employee_data)

print(employees)