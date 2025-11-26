def plastic_balance(lst):
    current = lst[:]
    while len(current) >= 2:
        sides_sum = current[0] + current[-1]
        middle_sum = sum(current[1:-1])

        if sides_sum == middle_sum:
            return current
        current = current[1:-1]
    if len(current) == 1 and current[0] == 0:
        return [0]
    else:
        return []
print(plastic_balance([1,2,3,4,5]))
print(plastic_balance([0,104,3,101,0,111]))
print(plastic_balance([1,-1]))
print(plastic_balance([0]))
print(plastic_balance([100,0,-100]))
print(plastic_balance([4,4]))
