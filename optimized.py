import time

actions = [
    ('action-1', 1, 1),
    ('action-2', 3, 4),
    ('action-3', 4, 5),
    ('action-4', 5, 7),]
"""    ('action-5',6000, 0.17),
    ('action-6',8000, 0.25),
    ('action-7',2200, 0.07),
    ('action-8',2600, 0.11),
    ('action-9',4800, 0.13),
    ('action-10',3400, 0.27),
    ('action-11',4200, 0.17),
    ('action-12',11000, 0.09),
    ('action-13',3800, 0.23),
    ('action-14',1400, 0.01),
    ('action-15',1800, 0.03),
    ('action-16',800, 0.08),
    ('action-17',400, 0.12),
    ('action-18',1000, 0.14),
    ('action-19',2400, 0.21),
    ('action-20',11400, 0.18)
    ]"""


"""Calcul le temps d'execution :
start_time = représente le début du programme

"""
start_time = time.time()


"""
Création des listes:
name = le nom des actions
action_value = la valeur des actions
benefit = le bénéfice attendu par action 
"""
name = list()
action_value = list()  #    wts
benefit = list()       #    vals


"""
Boucle qui va extraire les informations de la liste de tuple  "actions"
et ajouter les données aux listes
"""
for i in range(len(actions)):
    n, v, p = actions[i]
    benef = int(v * p)
    #benefit.append(benef)
    benefit.append(p)
    name.append(n)
    action_value.append(v)

"""
Création des variables :
capacity = le maximum pour acheter des actions
max_value = représente les colonnes du tableau
num_of_actions = le nombre d'actions
"""
capacity = 5
max_value = capacity + 1  #   w
num_of_actions = len(action_value)  #   h

"""
Création du tableau:
table = une liste qui contient autant de listes qu'il y a d'actions et ces listes contiennent autant
d'éléments que la capacité maximum.
Le tableau :  "lignes * nb-actions " et "colonnes * capacité"
"""
table = [[0 for i in range(max_value)] for elem in range(num_of_actions)]

"""
La boucle est créée à partir de la liste "action_value" et va itérer sur chaque lignes
"""
for index in range(len(action_value)):

    """La boucle est créée à partir de la capacité maximale et va itérer sur chaque colonnes"""
    for value in range(max_value):

        """Si la valeur de l'action est plus élevée que la capacité de la colonne, 
           On récupère la valeur de la cellule précédente (de la colonne)"""
        if action_value[index] > value:
            table[index][value] = table[index - 1][value]
            continue

        """Si la valeur de l'action est < à la capacité.
           prior_value = l'élément précédent de la colonne
           new_option_best = la valeur de l'action en cours de traitement + la valeur............. """
        prior_value = table[index - 1][value]
        new_option_best = benefit[index] + table[index - 1][value - action_value[index]]
        print ("\n\n\n" "\nbenefit[index] :", benefit[index], "\n+","\ntable[index - 1] :",table[index - 1], "\n\nvalue :",value, "\n-", "\naction_value[index] : ",action_value[index],"\nvalue - action_value[index] :", value - action_value[index],"\n=" "new_option_best :",new_option_best)

        table[index][value] = max(prior_value, new_option_best)
        #print(prior_value, new_option_best)
        #print(table)
          
result = max([x for y in table for x in y])
print(table)
print("--- %s seconds ---" % (time.time() - start_time))

"""
                                [0, 1, 1, 1, 1, 1] 
                                [0, 1, 1, 4, 5, 5]
                                [0, 1, 1, 4, 5, 6] 
                                [0, 1, 1, 4, 5, 7]
"""