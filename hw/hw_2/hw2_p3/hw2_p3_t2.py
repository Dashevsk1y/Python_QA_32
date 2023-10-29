# task 2

number = input("Введіть число, складається з чотирьох цифр: ")

if len(number) != 4:
    print("Введіть рівно чотири цифри.")
else:
    digit1 = int(number[0])
    digit2 = int(number[1])
    digit3 = int(number[2])
    digit4 = int(number[3])
    product = digit1 * digit2 * digit3 * digit4

    print(f"Добуток цифр дорівнює: {product}")
