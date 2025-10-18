def linear_search(arr, target):
    for index in range(len(arr)):
        if arr[index] == target:
            return index
    return -1

assert linear_search([5, 3, 7, 1, 4], 1) == 3
assert linear_search([10, 20, 30, 40], 30) == 2
assert linear_search([1, 2, 3, 4], 5) == -1
assert linear_search([1], 1) == 0
assert linear_search([], 1) == -1
print("OK!")
