def print_month_calendar(start_day, days_count):
    for _ in range(start_day):
        print("  ", end=" ")
    for day in range(1, days_count + 1):
        print(f"{day:2}", end=" ")
        if (start_day + day) % 7 == 0:
            print()
    print()
print_month_calendar(6, 31)
print("\n\n")
print_month_calendar(0, 28)