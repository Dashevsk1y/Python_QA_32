# task 1

num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))
num3 = float(input("Введіть третє число: "))

while True:
    print("Оберіть операцію:")
    print("1. Сума")
    print("2. Произведение")

    choice = input("Введіть номер операції (1 або 2): ")

    if choice == "1":
        result = num1 + num2 + num3
        print(f"Сума трьох чисел: {result}")
        break
    elif choice == "2":
        result = num1 * num2 * num3
        print(f"Произведение трьох чисел: {result}")
        break
    else:
        print(
            "Неправильний вибір операції. Будь ласка, введіть 1 або 2 для вибору операції."
        )
