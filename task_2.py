distance_1 = int(input("Введите километры: "))
distance_2 = int(input("Введите метры: "))
distance_1 = distance_1*1000
if distance_1>distance_2:
    print(distance_2, 'метра(ов)')
else:
    print(distance_1, 'метра(ов)')