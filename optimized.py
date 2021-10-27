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
actions = list()
benefit = list()


f = open ("actions_premiere_partie.csv")
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
table = [[0 for i in range(capacity)] for elem in range(num_of_actions)]
index = [["" for i in range(capacity)] for elem in range(num_of_actions)]

"""
La boucle est créée à partir de la liste "action_value" et va itérer sur chaque lignes
"""
for row in range(len(actions)):

    """La boucle est créée à partir de la capacité maximale et va itérer sur chaque colonnes"""
    for column in range(capacity):

        """
        Si la valeur de l'action est plus élevée que la capacité de la colonne, 
        On récupère la valeur de la cellule précédente (de la colonne)
        """
        if actions[row] > column:
            table[row][column] = table[row - 1][column]
            index[row][column] = index[row - 1][column]

            continue
        """
        Si la valeur de l'action est < à la capacité.
        prior_value = l'élément précédent de la colonne
        new_option_best = la valeur de l'action en cours de traitement + la valeur............. 
        """
        prior_value = table[row - 1][column]
        new_option_best = benefit[row] + table[row - 1][column - actions[row]]

        if prior_value < new_option_best :
            table[row][column] = new_option_best
            best_index = index[row - 1][column - actions[row]]
            new_index_best = str(row) + " " + str(best_index)
            index[row][column] = new_index_best
        else:
            table[row][column] = prior_value
            prior_index = index[row - 1][column]
            index[row][column] = prior_index

#result = max([x for y in table for x in y])
len_index = len(index) - 1
rez = index[len_index][-1].split()

result_name = list()
result_price = list()
gg = list()
for i in rez:
    elem = int(i)
    result_name.append(name[elem])
    result_price.append(actions[elem])
    gg.append(benefit[elem])

print("Pour un total de :", sum(result_price) / 100, "€")
print("Les actions les plus rentables sont :", ', '.join(result_name))
print("Pour un bénéfice de :", sum(gg) / 100, "€" )
print("--- %s seconds ---" % (time.time() - start_time))