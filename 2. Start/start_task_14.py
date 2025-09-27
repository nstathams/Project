def max_chislo(test):
    max_sum = 0
    c_sum = 0
    for num in test:
        c_sum += num
        if c_sum < 0:
            c_sum = 0
        max_sum = max(max_sum, c_sum)
    return max_sum
print(max_chislo([-2, 1, -3, 4, -1, 2, 1, -5, 4])) 
print(max_chislo([-1, -2, -3]))  
