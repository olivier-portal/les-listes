liste_entiers = [5, 12, 6, 70, 11, 23]

deuxième_valeur_liste = liste_entiers[1]
print(deuxième_valeur_liste)

    
def replace_value_liste():
    liste_entiers[3] = liste_entiers[2] + liste_entiers[4]
    return liste_entiers

new_liste = replace_value_liste()
print(new_liste)

dernière_valeur_liste = liste_entiers[-1]
print(dernière_valeur_liste)