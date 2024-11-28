L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]

liste = []
for i in L:
    if i % 2 == 0:
        liste.append(i)
        total = sum(liste)

print(total)