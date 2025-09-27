def snail(array):
    result = []
    while array:
        result += array.pop(0)
        if array and array[0]:
            for row in array:
                result.append(row.pop())
        if array:
            result += array.pop()[::-1]
        if array and array[0]:
            for row in array[::-1]:
                result.append(row.pop(0))
    return result
array = [
    [9, 2, 3, 4],
    [9, 2, 3, 4],
    [9, 2, 3, 4],
    [9, 2, 3, 1]
]
print(snail(array))
