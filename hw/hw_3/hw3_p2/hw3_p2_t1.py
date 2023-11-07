# task 1

while True:
    day_number = int(input("Введіть номер дня неделі (1-7): "))

    if day_number >= 1 and day_number <= 7:
        break
    else:
        print("Неправильний номер дня. Будь ласка, введіть число від 1 до 7.")

if day_number == 1:
    day_name = "понеділок"
elif day_number == 2:
    day_name = "вівторок"
elif day_number == 3:
    day_name = "середа"
elif day_number == 4:
    day_name = "четверг"
elif day_number == 5:
    day_name = "п'ятниця"
elif day_number == 6:
    day_name = "субота"
elif day_number == 7:
    day_name = "неділя"

print(f"День неділі з номером {day_number} - це {day_name}.")
