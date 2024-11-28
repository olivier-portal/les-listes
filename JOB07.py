L = [8, 24, 48, 2, 16]

liste = []
for i in L:
    if i % 3 == 0:
        liste.append(i)

print(len(liste))