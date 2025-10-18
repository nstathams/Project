import random
from collections import Counter
with open('words.csv', 'r') as file:
     dictionary = [line.strip() for line in file.readlines()]
# 1
def is_anagram_method1(s1, s2):
    if len(s1) != len(s2):
        return False
    s2_list = list(s2)
    for char in s1:
        if char in s2_list:
            s2_list.remove(char)
        else:
            return False
    return True
# 2
def is_anagram_method2(s1, s2):
    return sorted(s1) == sorted(s2)
# 3
def is_anagram_method3(s1, s2):
    from itertools import permutations
    if len(s1) > 7 or len(s2) > 7:
        return False
    return s2 in [''.join(p) for p in permutations(s1)]
# 4
def is_anagram_method4(s1, s2):
    return Counter(s1) == Counter(s2)
def find_anagrams_for_random_word(method_func):
    word = random.choice(dictionary)
    print(f"Исходное слово: {word}")
    anagrams = []
    for candidate in dictionary:
        if candidate != word and method_func(word, candidate):
            anagrams.append(candidate)
    print(f"Найдено анаграмм: {len(anagrams)}")
    print("Примеры:", anagrams[:10])
    return anagrams
find_anagrams_for_random_word(is_anagram_method1)
find_anagrams_for_random_word(is_anagram_method2)
find_anagrams_for_random_word(is_anagram_method3)
find_anagrams_for_random_word(is_anagram_method4)distance_1 = int(input("Введите километры: "))
distance_2 = int(input("Введите метры: "))
distance_1 = distance_1*1000
if distance_1>distance_2:
    print(distance_2, 'метра(ов)')
else:

    print(distance_1, 'метра(ов)')
