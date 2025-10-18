def most_f(n, q, array, queries):
    count = {}
    for num in array:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    counts = [(num, count[num]) for num in count]
    counts.sort()
    prefix_counts = []
    current_value = None
    current_count = 0
    for num, cnt in counts:
        if current_value is None or current_value != num:
            if current_value is not None:
                prefix_counts.append((current_value, current_count))
            current_value = num
            current_count = cnt
        else:
            current_count += cnt
    if current_value is not None:
        prefix_counts.append((current_value, current_count))
    results = []
    for i, j in queries:
        left_index = i - 1
        right_index = j - 1
        value_count = {}

        for idx in range(left_index, right_index + 1):
            value = array[idx]
            if value in value_count:
                value_count[value] += 1
            else:
                value_count[value] = 1

        most_frequent = max(value_count.values())
        results.append(most_frequent)
    return results

def test_most():
    n1, q1 = 10, 3
    array1 = [-1, -1, 1, 1, 1, 1, 3, 10, 10, 10]
    queries1 = [(2, 3), (1, 10), (5, 10)]
    expected1 = [1, 4, 3]
    assert most_f(n1, q1, array1, queries1) == expected1

    n6, q6 = 0, 0
    array6 = []
    queries6 = []
    expected6 = []
    assert most_f(n6, q6, array6, queries6) == expected6

    print("Тесты пройдены!")
    
test_most()
