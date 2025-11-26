def backg(items, time, weight_limit):
    x = [[0] * (weight_limit + 1) for _ in range(time + 1)]

    for value, timecost, weight_cost in items:
        for t in range(time, timecost - 1, -1):
            for y in range(weight_limit, weight_cost - 1, -1):
                x[t][y] = max(
                    x[t][y],
                    x[t - timecost][y - weight_cost] + value
                )

    return x[time][weight_limit]

items_1 = [(10, 5, 2), (15, 4, 3), (30, 7, 5)]
time_limit_1 = 10
weight_limit_1 = 10

items_2 = [(20, 6, 4), (15, 3, 3), (25, 5, 5), (10, 2, 2), (12, 4, 3)]
time_limit_2 = 12
weight_limit_2 = 10

items_3 = [(15, 5, 3), (12, 4, 2), (30, 7, 5), (25, 6, 4), (20, 3, 3)]
time_limit_3 = 15
weight_limit_3 = 12

items_4 = [(10, 4, 2), (20, 5, 3), (15, 3, 2), (25, 6, 4), (18, 4, 3)]
time_limit_4 = 13
weight_limit_4 = 11

print(backg(items_1, time_limit_1, weight_limit_1))
print(backg(items_2, time_limit_2, weight_limit_2))
print(backg(items_3, time_limit_3, weight_limit_3))
print(backg(items_4, time_limit_4, weight_limit_4))