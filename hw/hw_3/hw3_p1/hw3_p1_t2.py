# task 2

num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))
num3 = float(input("Введіть третє число: "))

while True:
    print("Оберіть операцію:")
    print("1. Максимум із трьох чисел")
    print("2. Мінімум із трьох чисел")
    print("3. Середнє арифметичне трьох чисел")

    choice = input("Введіть номер операції (1, 2 або 3): ")

    if choice == "1":
        result = max(num1, num2, num3)
        print(f"Максимум із трьох чисел: {result}")
        break
    elif choice == "2":
        result = min(num1, num2, num3)
        print(f"Мінімум із трьох чисел: {result}")
        break
    elif choice == "3":
        result = (num1 + num2 + num3) / 3
        print(f"Середнє арифметичне трьох чисел: {result}")
        break
    else:
        print(
            "Неправильний вибір операції. Будь ласка, введіть 1, 2 або 3 для вибору операції."
        )
