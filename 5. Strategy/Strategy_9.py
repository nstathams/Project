def backg(items, capacity):

    memo = {}

    def dopF(index, remaining_capacity):
        if index >= len(items) or remaining_capacity <= 0:
            return 0
        if (index, remaining_capacity) in memo:
            return memo[(index, remaining_capacity)]
        weight, value = items[index]
        without_current = dopF(index + 1, remaining_capacity)
        with_current = 0
        if weight <= remaining_capacity:
            with_current = value + dopF(index + 1, remaining_capacity - weight)
        result = max(without_current, with_current)
        memo[(index, remaining_capacity)] = result
        return result

    return dopF(0, capacity)

test_cases = [
    {
        "items": [(2, 5), (3, 8), (5, 15), (1, 3), (4, 10)],
        "capacity": 7,
        "expected": 18
    },
    {
        "items": [(6, 10), (8, 15), (12, 30)],
        "capacity": 5,
        "expected": 0
    },
    {
        "items": [(1, 1), (2, 6), (3, 10), (4, 15), (5, 20)],
        "capacity": 7,
        "expected": 22
    }
]

for i, case in enumerate(test_cases, 1):
    result = backg(case["items"], case["capacity"])
    status = "+" if result == case["expected"] else "-"
    print(f"\nТест {i}: {status}")
    print("# 1. Вес предмета")
    print("# 2. Стоимость предмета")
    print(f"  Ввод: предметы={case['items']}, вместимость - {case['capacity']}")
    print(f"  Ожидаемый результат: {case['expected']}")
    print(f"  Полученный результат: {result}")
    if result != case["expected"]:
        print("  Ошибочка")
