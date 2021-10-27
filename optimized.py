import time
import csv


"""
Calcul le temps d'execution :
start_time = représente le début du programme
"""
start_time = time.time()

"""
Création des listes:
name = le nom des actions
action_value = la valeur des actions
benefit = le bénéfice attendu par action 
"""
list_actions = list()
name = list()
actions = list()  #    wts
benefit = list() #vals

f= open ("actions_premiere_partie.csv")
myReader = csv.reader(f)
for row in myReader:
    list_actions.append(row)
del list_actions[0]


"""
Boucle qui va extraire les informations de la liste de tuple  "actions"
et ajouter les données aux listes
"""
for i in range(len(list_actions)):
    n, v, p = list_actions[i]
    value = int(v) * 100
    benef = value * (int(p) / 100)
    benefit.append(benef)
    name.append(n)
    actions.append(value)


"""
Création des variables :
capacity = le maximum pour acheter des actions
max_value = représente les colonnes du tableau
num_of_actions = le nombre d'actions
"""
cap = 50000
capacity = cap + 1
num_of_actions = len(actions)


"""
Création du tableau:
table = une liste qui contient autant de listes qu'il y a d'actions et ces listes contiennent autant
d'éléments que la capacité maximum.
Le tableau :  "lignes * nb-actions " et "colonnes * capacité"
"""
tableau = [[0 for i in range(capacity)] for elem in range(num_of_actions)]
nomtab = [["" for i in range(capacity)] for elem in range(num_of_actions)]

"""
La boucle est créée à partir de la liste "action_value" et va itérer sur chaque lignes
"""
for ligne in range(len(actions)):

    """La boucle est créée à partir de la capacité maximale et va itérer sur chaque colonnes"""
    for colonne in range(capacity):

        """
        Si la valeur de l'action est plus élevée que la capacité de la colonne, 
        On récupère la valeur de la cellule précédente (de la colonne)
        """
        if actions[ligne] > colonne:
            tableau[ligne][colonne] = tableau[ligne - 1][colonne]
            nomtab[ligne][colonne] = nomtab[ligne - 1][colonne]
            continue

        """
        Si la valeur de l'action est < à la capacité.
        prior_value = l'élément précédent de la colonne
        new_option_best = la valeur de l'action en cours de traitement + la valeur............. 
        """
        prior_colonne = tableau[ligne - 1][colonne]
        new_option_best = benefit[ligne] + tableau[ligne - 1][colonne - actions[ligne]]

        prior_name = nomtab[ligne - 1][colonne]
        best = ', ' + nomtab[ligne - 1][colonne - actions[ligne]]
        new_name_best = name[ligne] + best

        if prior_colonne < new_option_best :
            tableau[ligne][colonne] = new_option_best
            nomtab[ligne][colonne] = new_name_best
        else:
            tableau[ligne][colonne] = prior_colonne
            nomtab[ligne][colonne] = prior_name

result = max([x for y in tableau for x in y])
result_name = len(nomtab) - 1
print(nomtab[result_name][-1])
print(result / 100)
print("--- %s seconds ---" % (time.time() - start_time))
