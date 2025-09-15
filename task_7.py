def find_diameter(radius):
    return 2 * radius
radius = int(input("Введите радиус окружности: "))
diameter = find_diameter(radius)
print(f"Диаметр окружности: {diameter}")


def sum_100_to_500():
    return sum(range(100, 501))

sum_1 = sum_100_to_500()
print(f"Сумма чисел от 100 до 500: {sum_1}")



def sum_a_to_500(a):
    if a >= 500:
        return "Ошибка: 'a' должно быть меньше 500"
    return sum(range(a, 501))
a = int(input("Введите значение a (a < 500): "))
sum_2 = sum_a_to_500(a)
print(f"Сумма чисел от {a} до 500: {sum_2}")