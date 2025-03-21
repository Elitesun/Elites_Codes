nlist = []
for _ in range(int(input("Enter number of students: "))):
    name = input("Enter name: ")
    score = float(input("Enter score: "))
    nlist.append([name, score])

# Sort list by the score
nlist.sort(key=lambda x: x[1])

# Find the second lowest score
minscore = nlist[0][1]
secondmin = None
for score in nlist:
    if score[1] > minscore:
        secondmin = score[1]
        break

# Collect names of students with the second lowest score
secondlist = [name for name, score in nlist if score == secondmin]

# Print names in alphabetical order
for name in sorted(secondlist):
    print(name)