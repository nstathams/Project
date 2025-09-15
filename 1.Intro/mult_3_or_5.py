def mult_3_or_5(number):
    # ВАШЕ РЕШЕНИЕ ТУТ
    # Если число отрицательное, возвращаем 0
    if number <= 0:
        return 0

    total_sum = 0

    # Перебираем все числа от 1 до номер-1
    for i in range(1, number):
        # Проверяем кратность 3 или 5
        if i % 3 == 0 or i % 5 == 0:
            total_sum += i

    return total_sum


def test():
    test_cases = [
        (3, 0),  # Test 1
        (4, 3),  # Test 2
        (5, 3),  # Test 3
        (6, 8),  # Test 4
        (7, 14),  # Test 5
        (10, 23),  # Test 6
        (20, 78),  # Test 7
        (10, 23)  # Test 8
    ]

    for i, (input_num, expected) in enumerate(test_cases, 1):
        try:
            result = mult_3_or_5(input_num)
            if result != expected:
                exit(i)
        except Exception:
            exit(i)

    return True


if __name__ == "__main__":
    test()
    exit(0)