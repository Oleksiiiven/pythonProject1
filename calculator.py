def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Ділити на нуль not appropriate!"

while True:
    print("Обери дію будь ласка:")
    print("1. Додавати")
    print("2. Віднімати")
    print("3. Множити")
    print("4. Ділити")
    print("5. Геть, я стомивсі")

    choice = input("Який твій вибір (1/2/3/4/5): ")

    if choice == '5':
        print("Ще побачимось!")
        break

    num1 = float(input("Введи перше число: "))
    num2 = float(input("Введи друге число: "))

    if choice == '1':
        print("А ось і результат:", add(num1, num2))
    elif choice == '2':
        print("А ось і результат:", subtract(num1, num2))
    elif choice == '3':
        print("А ось і результат:", multiply(num1, num2))
    elif choice == '4':
        print("А ось і результат:", divide(num1, num2))
    else:
        print("Ти щось не то робиш")
