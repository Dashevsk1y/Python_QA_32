# task 3

meters = float(input("Введіть кількість метрів: "))

while True:
    print("Оберіть одиницю вимірювання для переведення:")
    print("1. Метри в милі")
    print("2. Метри в дюйми")
    print("3. Метри в ярди")

    choice = input("Введіть номер операції (1, 2 або 3): ")

    if choice == "1":
        miles = meters * 0.000621371  # перетворення метрів в милі
        print(f"{meters} метрів дорівнює {miles} миль")
        break
    elif choice == "2":
        inches = meters * 39.3701  # перетворення метрів в дюйми
        print(f"{meters} метрів дорівнює {inches} дюймів")
        break
    elif choice == "3":
        yards = meters * 1.09361  # перетворення метрів в ярди
        print(f"{meters} метрів дорівнює {yards} ярдів")
        break
    else:
        print(
            "Неправильний вибір операції. Будь ласка, введіть 1, 2 або 3 для вибору операції."
        )
