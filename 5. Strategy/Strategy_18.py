def move_zero(lst):
    non_zeros = []
    zero_count = 0
    for item in lst:
        if item == 0:
            zero_count += 1
        else:
            non_zeros.append(item)
    return non_zeros + [0] * zero_count

print(move_zero([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))
print(move_zero([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))

