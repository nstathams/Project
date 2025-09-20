def race(v1, v2, s):
    if v1 >= v2:
        return None
    time_hours = s / (v2 - v1)
    hours = int(time_hours)
    minutes = int((time_hours - hours) * 60)
    seconds = int(((time_hours - hours) * 60 - minutes) * 60)
    return [hours, minutes, seconds]
v1 = int(input('Введите скорость первой черепашки:' ))
v2 = int(input('Введите скорость второй черепашки:' ))
s = int(input('Введите скорость первой черепашки:' ))
result = race(v1, v2, s)
if result is None:
    print("Вторая черепаха никогда не догонит первую! :( ")
else:
    print("Время встречи: {} ч {} мин {} сек".format(result[0], result[1], result[2]))
