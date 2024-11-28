L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

l_between25_90 = [i for i in L if i >= 25 and i <= 90]

total = sum(l_between25_90)

print(total)