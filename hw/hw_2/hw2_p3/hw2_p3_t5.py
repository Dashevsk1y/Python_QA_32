# task 5

number = int(input("Введіть чотирьохзначне число: "))

reversed_number = 0
while number > 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number = number // 10

print(f"Результат: {reversed_number}")
