def max_sum_after_swaps(t, test_):
    results = []

    for n, k, a, b in test_:
        a_sorted = sorted(a)
        b_sorted = sorted(b, reverse=True)
        total = sum(a_sorted)

        for i in range(k):
            if b_sorted[i] > a_sorted[i]:
                total += b_sorted[i] - a_sorted[i]
            else:
                break

        results.append(total)

    return results

t = int(input())
test_ = []

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    test_.append((n, k, a, b))

answers = max_sum_after_swaps(t, test_)
for ans in answers:
    print(ans)
# пример с github для использования
"""
5
2 1
1 2
3 4
5 5
5 5 6 6 5
1 2 5 4 3
5 3
1 2 3 4 5
10 9 10 10 9
4 0
2 2 4 3
2 4 2 3
4 4
1 2 2 1
4 4 5 4
"""