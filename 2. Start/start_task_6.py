def sorted_numbers(k1, k2):
    str_k1 = str(k1)
    str_k2 = str(k2)
    sorted1 = ''.join(sorted(str_k1))
    sorted2 = ''.join(sorted(str_k2))
    return sorted1 == sorted2
k1 = int(input("Введите число k1: "))
k2 = k1 + 1
n = 1
result = False
while not result:
    ck1 = k1 * n
    ck2 = k2 * n
    result = sorted_numbers(ck1, ck2)
    if not result:
        n += 1
print(f"Наименьшее n: {n}")
