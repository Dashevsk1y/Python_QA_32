# task 3

meters = float(input("Введіть кількість метрів: "))

centimeters = meters * 100
decimeters = meters * 10
millimeters = meters * 1000
kilometers = meters / 1000

print(f"{meters} метрів = {centimeters} сантиметрів")
print(f"{meters} метрів = {decimeters} дециметрів")
print(f"{meters} метрів = {millimeters} міліметрів")
print(f"{meters} метрів = {kilometers} кілометрів (милі)")
