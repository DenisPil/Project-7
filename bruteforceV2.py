import numpy as np
import itertools
import time

actions = [
    ('action-1',2000, 0.05),
    ('action-2',3000, 0.2),
    ('action-3',5000, 0.15),
    ('action-4',7000, 0.2),
    ('action-5',6000, 0.17),
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
    ]

benefit = list()
name = list()
action_value = list()
sum_of_benefit = list()
actions_link_to_profit = list()
sum_of_actions = list()

for i in range(len(actions)):
    n, v, p = actions[i]
    benef = int(v * p)
    benefit.append(benef)
    name.append(n)
    action_value.append(v)


def force_brut():

    compteur = 0
    for v in itertools.product([0, 1], repeat=20):
        compteur += 1

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
    #print(actions_link_to_profit)

def best_combiantion():
    result = list()
    actions_link_to_profit_sorted = (sorted(actions_link_to_profit, key=lambda t:t[0], reverse=True))
    for elem in actions_link_to_profit_sorted:
        actions = list()
        n = list()
        for i in elem[1]:
            
            actions.append(action_value[i])
            n.append(name[i])
        gg = sum(actions)
        if gg <= 50000:    
            result.append((n, gg, elem[0]))
            #break    
    sorted_result = (sorted(result, key=lambda t:t[1], reverse=True))
    print("Pour un total de :", int(sorted_result[0][1] / 100), "€", "les actions les plus rentable sont :", (sorted_result[0][0]), "pour un bénéfice de :", sorted_result[0][2]/100, "€" )

start_time = time.time()
force_brut()
best_combiantion()
print("--- %s seconds ---" % (time.time() - start_time))



