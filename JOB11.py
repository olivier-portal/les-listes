def my_list():
    liste = []
    liste.extend([7, 11, 42, 39, 2])
    for i in range(len(liste)):
        liste[i] += 1
    return liste
    
show_list = my_list()
print(show_list)
        
        