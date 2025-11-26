def compare_strings():
    str1 = input().strip()
    str2 = input().strip()
    str1_lower = str1.lower()
    str2_lower = str2.lower()
    if str1_lower < str2_lower:
        print("-1")
    elif str1_lower > str2_lower:
        print("1")
    else:
        print("0")
compare_strings()
