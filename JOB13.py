def supp_doubleNumber_inliste():
    list = [0, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40] #define list
    list_length = 0
# Iterating through List in order to find the list's length
    for _ in list:
        list_length += 1
    # print(list_length) Find list length
    for i in range(list_length): #firts pass
        for j in range(list_length - 1): #go through all list
            if list[j] > list[j + 1]: #compare if an element is bigger than the next one
                list[j], list[j + 1] = list[j + 1], list[j] #reorder list
                if list[j] == list[j + 1]:
                    del list[j + 1]
    return list
        
clean_list = supp_doubleNumber_inliste()

print(clean_list)