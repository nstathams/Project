def month(startday, days):
    for i in range(startday):
        print("  ", end=" ")
    for day in range(1, days + 1):
        print(f"{day:2}", end=" ")
        if (startday + day) % 7 == 0:
            print()
    print()
month(6, 31)
print("\n\n")
month(0, 28)
