def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
sorted_numbers = [1, 2, 3, 4, 5, 6, 7]
index_of_four = binary_search(sorted_numbers, 4)
print(index_of_four)
index_of_eight = binary_search(sorted_numbers, 8)
print(index_of_eight)
try:
    assert binary_search([1, 2, 3, 4, 5, 6, 7], 4) == 3, "Ошибка"
    assert binary_search([1, 2, 3, 4, 5, 6, 7], 6) == 5, "Ошибка"
    assert binary_search([1, 2, 3, 4, 5, 6, 7], 1) == 0, "Ошибка"
    assert binary_search([1, 2, 3, 4, 5, 6, 7], 8) == -1, "Ошибка"
    assert binary_search([], 1) == -1, "Ошибка"
    print("Все тесты пройдены!")
except AssertionError as DAA:
    print(DAA)
