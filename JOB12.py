# def liste(list=[8, 24, 27, 48, 2, 16, 9, 7, 84, 91]):
#     list_length = 0
# # Iterating through List
#     for _ in list:
#         list_length += 1
#     # print(list_length) Find list length
#     for i in range(list_length): #firts pass
#         for j in range(list_length - 1): #go through all list
#             if list[j] > list[j + 1]: #compare if an element is bigger than the next one
#                 list[j], list[j + 1] = list[j + 1], list[j] #reorder list
#     return list
        
# ordered_list = liste()

# print(ordered_list)

L=[8, 24, 27, 48, 2, 16, 9, 7, 84, 91]
for i in range(len(L)): 
    for j in range(i+1, len(L)): 
        if L[i] > L[j]: L[i], L[j] = L[j], L[i]
print(L)