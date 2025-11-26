def knapsack(n, capacity, items):
    # dp[w] — максимальная стоимость для вместимости w
    dp = [0] * (capacity + 1)

    for weight, value in items:
        # Обновляем dp от конца к началу, чтобы не использовать один предмет дважды
        for w in range(capacity, weight - 1, -1):
            dp[w] = max(dp[w], dp[w - weight] + value)

    return dp[capacity]


# Чтение входных данных
n, capacity = map(int, input().split())
items = []
for _ in range(n):
    weight, value = map(int, input().split())
    items.append((weight, value))

# Вывод результата
print(knapsack(n, capacity, items))