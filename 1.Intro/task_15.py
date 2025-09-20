def year_(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False
def daysmonth(month, year):
    days = {
        1: 31,  # Январь
        2: 29 if year_(year) else 28,  # Февраль
        3: 31,  # Март
        4: 30,  # Апрель
        5: 31,  # Май
        6: 30,  # Июнь
        7: 31,  # Июль
        8: 31,  # Август
        9: 30,  # Сентябрь
        10: 31,  # Октябрь
        11: 30,  # Ноябрь
        12: 31  # Декабрь
    }
    if month in days:
        return days[month]
    else:
        return "Месяц введен неправильно!!!!!!!!!!!"
month = int(input("Введите номер месяца от 1 до 12: "))
year = int(input("Введите год: "))
print(daysmonth(month, year))
