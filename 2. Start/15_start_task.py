def calculate_(sequence):
    sequence = sequence.upper().replace(" ", "")
    g_count = sequence.count('G')
    c_count = sequence.count('C')
    total_ = len(sequence)
    g_per = (g_count / total_) * 100 if total_ > 0 else 0
    c_per = (c_count / total_) * 100 if total_ > 0 else 0
    return g_per, c_per
def is_palindrome(sequence):
    sequence = sequence.upper().replace(" ", "")
    complement = []
    for base in sequence:
        if base == 'A':
            complement.append('T')
        elif base == 'T':
            complement.append('A')
        elif base == 'C':
            complement.append('G')
        elif base == 'G':
            complement.append('C')
    reverse_complement = ''.join(complement)[::-1]
    return sequence == reverse_complement
sequence = "TGGATCCA"
g_per, c_per = calculate_(sequence)
print(f"Процент G: {g_per:.2f}%")
print(f"Процент C: {c_per:.2f}%")
if is_palindrome(sequence):
    print("Последовательность является палиндромом.")
else:
    print("Последовательность не является палиндромом.")