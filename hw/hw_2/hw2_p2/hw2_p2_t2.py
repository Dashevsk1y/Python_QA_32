# task 2

a = float(input('Введіть зарплату за місяць:'))
b = float(input('Введіть суму щомісячного платежу по кредиту у банку:'))
c = float(input('Введіть заборгованість за комунальні послуги:'))

d = int(a - b - c)

print(f"Після всіх виплат залишиться: {d} грн")
