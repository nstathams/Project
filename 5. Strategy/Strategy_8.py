def backg(items, capacity):
    if not items or capacity <= 0:
        return 0
    weight, value = items[0]
    remaining_items = items[1:]
    without_current = backg(remaining_items, capacity)
    if weight <= capacity:
        with_current = value + backg(remaining_items, capacity - weight)
        return max(without_current, with_current)
    else:
        return without_current

test_cases = [
    {
        "items": [(2, 10), (3, 15), (5, 30)],
        "capacity": 5,
        "expected": 30
    },
    {
        "items": [(2, 10), (3, 15), (5, 30), (7, 20), (1, 5), (4, 10)],
        "capacity": 10,
        "expected": 50
    },
    {
        "items": [(2, 20), (3, 15), (5, 30), (1, 25), (4, 10)],
        "capacity": 7,
        "expected": 55
    }
]

for i, case in enumerate(test_cases, 1):
    result = backg(case["items"], case["capacity"])
    status = "+" if result == case["expected"] else "-"
    print(f"\nТест {i}: {status}")
    print("# 1. Вес предмета")
    print("# 2. Стоимость предмета")
    print(f"  Предметы {case['items']}, вместимость - {case['capacity']}")
    print(f"  Ожидаемый результат: {case['expected']}")
    print(f"  Полученный результат: {result}")
    if result != case["expected"]:
        print("  Ошибочка")
