
def convert(value, to_bytes):
    return value * 1024 if to_bytes else value / 1024


def main():
    print("Конвертация байтов и килобайтов")
    print("1 - КБ → Байты")
    print("2 - Байты → КБ")

    x = input("Выберите действие (1/2): ")
    value = float(input("Введите значение: "))

    if x == '1':
        result = convert(value, True)
        print(f"{value} КБ = {result} байт")
    elif x == '2':
        result = convert(value, False)
        print(f"{value} байт = {result:.2f} КБ")
    else:
        print("Неверный выбор!")


if __name__ == "__main__":
    main()