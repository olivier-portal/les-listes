# def supp_doubleNumber_inliste():
#     list = [0, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40] #define list
#     list_length = 0
# # Iterating through List in order to find the list's length
#     for _ in list:
#         list_length += 1
#     # Find list length
#     i = 0
#     while i < list_length: #firts pass
#         j= i + 1
#         while j < list_length: #go through all list
#             if list[i] == list[j]: #if a double is find
#                 del list[j] #suppress double
#                 list_length -= 1 # in order not to be out of range
#             else:
#                 j += 1 #go o next element
#         i += 1
#     return list
        
# clean_list = supp_doubleNumber_inliste()

# print(clean_list)

L = [0, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
# L = list(dict.fromkeys(L))
L = [x for i, x in enumerate(L) if x not in L[:i]]
print(L)