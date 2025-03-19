list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
for index, (item1, item2) in enumerate(zip(list1, list2)):
    print(f"Index {index}: {item1} - {item2}")
# Output:
# Index 0: a - 1
# Index 1: b - 2
# Index 2: c - 3



seasons = ['Spring', 'Summer', 'Fall', 'Winter']
target_season = 'Fall'
for index, season in enumerate(seasons):
    if season == target_season:
        print(f"{target_season} is at index {index}")
        break
# Output: Fall is at index 2



seasons = ['Spring', 'Summer', 'Fall', 'Winter']
season_dict = {index: season for index, season in enumerate(seasons)}
print(season_dict)
# Output: {0: 'Spring', 1: 'Summer', 2: 'Fall', 3: 'Winter'}




seasons = ['Spring', 'Summer', 'Fall', 'Winter']
modified_seasons = [f"{index}-{season}" for index, season in enumerate(seasons)]
print(modified_seasons)
# Output: ['0-Spring', '1-Summer', '2-Fall', '3-Winter']





seasons = ['Spring', 'Summer', 'Fall', 'Winter']
for index, season in enumerate(seasons, start=1):
    print(f"Index {index}: {season}")
# Output:
# Index 1: Spring
# Index 2: Summer
# Index 3: Fall
# Index 4: Winter

