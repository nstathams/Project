a = [1, 2, 2, 2, 2, 4, 5, 4, 6]
b = [2, 5]
result = []
for i in a:
    if i not in b:
        result.append(i)
print(result)
