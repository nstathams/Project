from itertools import permutations

def gta(limit, *numbers):
    digits = []
    for num in numbers:
        for d in str(num):
            digits.append(int(d))
    unique_sorted = sorted(set(digits))
    base_list = unique_sorted[:limit]

    total_sum = 0
    for length in range(1, limit + 1):
        for perm in permutations(base_list, length):
            total_sum += sum(perm)

    return total_sum
# Пример 1
print(gta(7, 123489, 5, 67))  # Вернет 328804, базовый список = [1, 2, 3, 4, 5, 6, 7]

# Пример 2
print(gta(8, 12348, 47, 3639))  # Вернет 3836040, базовый список = [1, 2, 3, 4, 6, 7, 8, 9]