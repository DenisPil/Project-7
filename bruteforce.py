import numpy as np
import itertools


list_action = np.array([20, 30, 50, 70, 60, 80, 22, 26, 48, 34, 42, 110, 38, 14, 18, 8, 4, 10, 24, 114]) #])#
list_pourcentage =  np.array([0.05, 0.2, 0.15, 0.2, 0.17, 0.25, 0.07, 0.11, 0.13, 0.27, 0.17, 0.09, 0.23, 0.01, 0.03, 0.08, 0.12, 0.14, 0.21, 0.18])
list_action_name = ["action-1", "action-2", "action-3", "action-4", "action-5", "action-6", "action-7", "action-8", "action-9", "action-10", "action-11", "action-12", "action-13"," action-14", "action-15", "action-16", "action-17", "action-18", "action-19", "action-20"] 
list_benef = (list_action * list_pourcentage)
list_rez_sorted = list()
dict_profit_and_action_name = dict()
list_matrix = list()
list_calcul_benef = list()
jojo = list()
best = list()

def force_brut():

    compteur = 0
    for v in itertools.product([0, 1], repeat=20):
        compteur += 1
        print(compteur)
        list_binary = np.array([v])
        list_calcul_benef = list_binary * list_benef
        list_matrix = list_action * list_binary

        for i in list_calcul_benef:
            sum_of_profits = sum(i)
            list_rez_sorted.append(sum_of_profits)
            action_value = list()
            for key, elem in enumerate(i):
                if elem != 0.0:
                    action_value.append(list_action[key])
                    dict_profit_and_action_name.update({sum_of_profits: action_value})

def calcul_action_value():

    for  elem in dict_profit_and_action_name.items()  :
        actions_value = sum(elem[1])
        jojo.append([elem[0], elem[1], actions_value])



def best_combination():
    test = list()
    actions_value_sorted =(sorted(jojo, key=lambda t:t[2], reverse=True))
    for elem in actions_value_sorted:
        if elem[2] <= 500:
            test.append(elem)
    best_profit =(sorted(test, key=lambda t:t[0], reverse=True))


    for elem in best_profit[0][1]:
        for key, action in enumerate(list_action):
            if elem == action:
                best.append(list_action_name[key])
    print("Pour un total de :", best_profit[0][2], "€", "les actions les plus rentables sont :", best, "pour un bénéfice de :", best_profit[0][0])



force_brut()
calcul_action_value()
best_combination()

