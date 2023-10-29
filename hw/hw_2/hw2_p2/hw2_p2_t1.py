# task 1

num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))
num3 = float(input("Введіть третє число: "))

if num1 == 0 or num2 == 0 or num3 == 0:
    print("Увага! Ділення на нуль неможливе.")
else:
    sum_of_numbers = num1 + num2 + num3
    product_of_numbers = num1 * num2 * num3

    print(f"Сума чисел: {sum_of_numbers}")
    print(f"Добуток чисел: {product_of_numbers}")
