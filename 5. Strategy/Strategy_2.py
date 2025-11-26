def flowers_combination(flowers):
    n = len(flowers)
    return 2**n - 1

flowers_set1 = {"rose", "jasmine", "lily"}
flowers_set2 = {"orchid", "tulip", "violet", "daisy"}
flowers_set3 = {"lavender", "sunflower"}

print(flowers_combination(flowers_set1))
print(flowers_combination(flowers_set2))
print(flowers_combination(flowers_set3))