def find_longest_recurring_cycle(limit):
    def cycle_length(d):
        seen = {}
        value = 1
        position = 0
        while value != 0:
            if value in seen:
                return position - seen[value]
            seen[value] = position
            value = (value * 10) % d
            position += 1
        return 0
    max_length = 0
    result_d = 0
    for d in range(2, limit):
        if d % 2 == 0 or d % 5 == 0:
            continue
        length = cycle_length(d)
        if length > max_length:
            max_length = length
            result_d = d
    return result_d, max_length

result_d, max_length = find_longest_recurring_cycle(1000)
print(f"d = {result_d}, Полож. повт. циклы = {max_length}")
