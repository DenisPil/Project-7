import numpy as np
import itertools
import time
import csv

list_actions = list()
benefit = list()
name = list()
action_value = list()
sum_of_benefit = list()
actions_link_to_profit = list()
sum_of_actions = list()


f = open ("actions_premiere_partie.csv")
myReader = csv.reader(f)
for row in myReader:
    list_actions.append(row)
del list_actions[0]

for i in range(len(list_actions)):
    n, v, p = list_actions[i]
    value = int(v) * 100
    benef = value * (int(p) / 100)
    benefit.append(benef)
    name.append(n)
    action_value.append(value)


def force_brut():

    for v in itertools.product([0, 1], repeat=20):
        list_binary = np.array([v])
        list_calcul_benef = list_binary * benefit

        for i in list_calcul_benef:
            sum_of_profits = sum(i)
            sum_of_benefit.append(sum_of_profits)
            keys = list()

            for key, elem in enumerate(i):
                if elem != 0.0:
                    keys.append(key)
            actions_link_to_profit.append((sum_of_profits, keys))


def best_combiantion():

    result = list()
    actions_link_to_profit_sorted = (sorted(actions_link_to_profit, key=lambda t:t[0], reverse=True))
    for elem in actions_link_to_profit_sorted:
        actions = list()
        n = list()

        for i in elem[1]:
            actions.append(action_value[i])
            n.append(name[i])
        actions_sum = sum(actions)
        if actions_sum <= 50000:    
            result.append((n, actions_sum, elem[0]))
            #break    
    sorted_result = (sorted(result, key=lambda t:t[1], reverse=True))
    print("Pour un total de :", int(sorted_result[0][1] / 100), "€")
    print("Les actions les plus rentables sont :", (sorted_result[0][0]))
    print("Pour un bénéfice de :", sorted_result[0][2] / 100, "€" )


start_time = time.time()
force_brut()
best_combiantion()
print("--- %s seconds ---" % (time.time() - start_time))



