def powerk(n, k):
    count = 0
    power = k
    while n // power > 0:
        count += n // power
        power *= k
    return count
print(powerk(10, 2))