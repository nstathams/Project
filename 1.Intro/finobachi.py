cur = 1
prev = 0
a = 0
while cur <= 4000000:
    tek = cur
    cur = cur + prev
    prev = tek
    if cur % 2 == 0:
        a = a + cur
print(a)
