# task 2

while True:
    month_number = int(input("Введіть номер місяця (1-12): "))

    if month_number >= 1 and month_number <= 12:
        break
    else:
        print("Неправильний номер місяця. Будь ласка, введіть число від 1 до 12.")

if month_number == 1:
    month_name = "січень"
elif month_number == 2:
    month_name = "лютий"
elif month_number == 3:
    month_name = "березень"
elif month_number == 4:
    month_name = "квітень"
elif month_number == 5:
    month_name = "травень"
elif month_number == 6:
    month_name = "червень"
elif month_number == 7:
    month_name = "липень"
elif month_number == 8:
    month_name = "серпень"
elif month_number == 9:
    month_name = "вересень"
elif month_number == 10:
    month_name = "жовтень"
elif month_number == 11:
    month_name = "листопад"
elif month_number == 12:
    month_name = "грудень"

print(f"Місяць з номером {month_number} - це {month_name}.")
