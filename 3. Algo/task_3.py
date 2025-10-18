import random

def quick_sort_deck(deck):
    if len(deck) < 4:
        return sorted(deck)
    pivot = random.choice(deck)
    left = [card for card in deck if card < pivot]
    right = [card for card in deck if card > pivot]
    return quick_sort_deck(left) + [pivot] + quick_sort_deck(right)

deck = [6, 2, 1, 5, 4, 3]
sorted_deck = quick_sort_deck(deck)
print(sorted_deck)
