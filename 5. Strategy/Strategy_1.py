sea_fish        = ["shark", "flounder", "tuna", "cod", "herring", "Marlin"]
freshwater_fish = ["Asp", "Pike", "Carp", "Salmon", "Ide", "Trout"]

fish = sea_fish + freshwater_fish
all_fish = [x.capitalize() for x in fish]

n = len(all_fish)
for i in range(n):
    for j in range(0, n - i - 1):
        if all_fish[j] > all_fish[j + 1]:
            all_fish[j], all_fish[j + 1] = all_fish[j + 1], all_fish[j]
print(all_fish)
