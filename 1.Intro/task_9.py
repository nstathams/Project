a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))
m = a
if b > m:
    m = b

if c > m:
    m = c
print(f"Максимальное значение: {m}")