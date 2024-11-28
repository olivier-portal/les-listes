def liste(list=[8, 24, 27, 48, 2, 16, 9, 7, 84, 91]):
    index= 0
    index2=1
    for index in range(len(list)):
        if list[index] > list[index2]:
            list[index], list[index2] = list[index2], list[index]
            index += 1
            index2 += 1
    return list
        
ordered_list = liste()

print(ordered_list)