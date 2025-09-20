def square_digits(number):
    empty = ''
    for k in str(number):
        empty += str(int(k)**2)
    return int(empty)
result = square_digits(235)
print("Результат:", result)
