def fill(arr, method):
    if not arr:
        return []
    if all(x is None for x in arr):
        return arr[:]
    n = len(arr)
    result = arr[:]
    if method == -1:
        for i in range(n - 2, -1, -1):
            if result[i] is None and result[i + 1] is not None:
                result[i] = result[i + 1]
    elif method == 1:
        for i in range(1, n):
            if result[i] is None and result[i - 1] is not None:
                result[i] = result[i - 1]

    elif method == 0:
        left_dist = [float('inf')] * n
        right_dist = [float('inf')] * n

        last_val = None
        for i in range(n):
            if result[i] is not None:
                last_val = result[i]
                left_dist[i] = 0
            elif last_val is not None:
                left_dist[i] = left_dist[i - 1] + 1
        last_val = None
        for i in range(n - 1, -1, -1):
            if result[i] is not None:
                last_val = result[i]
                right_dist[i] = 0
            elif last_val is not None:
                right_dist[i] = right_dist[i + 1] + 1 if i + 1 < n else float('inf')
        for i in range(n):
            if result[i] is None:
                left_val = result[i - left_dist[i]] if left_dist[i] != float('inf') else None
                right_val = result[i + right_dist[i]] if right_dist[i] != float('inf') else None

                if left_dist[i] < right_dist[i]:
                    result[i] = left_val
                elif right_dist[i] < left_dist[i]:
                    result[i] = right_val
                else:
                    if left_val is None:
                        result[i] = right_val
                    elif right_val is None:
                        result[i] = left_val
                    else:
                        result[i] = min(left_val, right_val)

    return result
arr = [None, 1, None, None, None, 2, None]

print(fill(arr, -1))
print(fill(arr,  0))
print(fill(arr,  1))

