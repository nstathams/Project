import math
def format_number(num):
    if isinstance(num, str): 
        return num
    elif num >= 10 ** 6 or num <= -10 ** 6:
        return f"{num:.2e}" 
    else:
        return f"{num:.2f}"
def complexity_table(sizes, max_value=10 ** 25):
    print("Рост количества операций для разных O-сложностей:")
    print(
        f"{'n':<10}{'O(1)':<15}{'O(log n)':<15}{'O(sqrt(n))':<15}{'O(n)':<15}{'O(n log n)':<15}{'O(n**2)':<15}{'O(n**3)':<15}{'O(2**n)':<15}{'O(n!)':<15}")
    print("-" * 150)

    for n in sizes:
        o_1 = 1
        o_log_n = math.log2(n) if n > 0 else 0
        o_sqrt_n = math.sqrt(n)
        o_n = n
        o_n_log_n = n * o_log_n if n > 0 else 0
        if o_n_log_n > max_value:
            o_n_log_n = " "

        o_n2 = n ** 2
        if o_n2 > max_value:
            o_n2 = " "

        o_n3 = n ** 3
        if o_n3 > max_value:
            o_n3 = " "

        o_2n = 2 ** n
        if o_2n > max_value:
            o_2n = " "

        try:
            o_n_fact = math.factorial(n)
            if o_n_fact > max_value:
                o_n_fact = " "
        except OverflowError:
            o_n_fact = " "
        print(
            f"{n:<10}{format_number(o_1):<15}{format_number(o_log_n):<15}{format_number(o_sqrt_n):<15}{format_number(o_n):<15}{format_number(o_n_log_n):<15}{format_number(o_n2):<15}{format_number(o_n3):<15}{format_number(o_2n):<15}{format_number(o_n_fact):<15}")
sizes = [1, 10, 100, 1000, 10000]
complexity_table(sizes)
