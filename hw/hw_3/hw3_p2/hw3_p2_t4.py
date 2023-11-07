# task 4

num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))

if num1 == num2:
    print("Числа рівні.")
else:
    if num1 < num2:
        print(f"Числа у порядку зростання: {num1}, {num2}")
    else:
        print(f"Числа у порядку зростання: {num2}, {num1}")
