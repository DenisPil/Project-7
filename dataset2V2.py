import csv
import time
import math

start_time = time.time()

def knapSack(capacity, actions, benefit, num_of_actions, name):
    table = [[0 for w in range(capacity + 1)]for i in range(num_of_actions + 1)]

    for row in range(num_of_actions + 1):
        for column in range(capacity + 1):
            if row == 0 or column == 0:
                table[row][column] = 0
            elif actions[row - 1] <= column:
                table[row][column] = max(benefit[row - 1]
                  + table[row - 1][column - actions[row - 1]],
                               table[row - 1][column])
            else:
                table[row][column] = table[row - 1][column]
 
    res = table[num_of_actions][capacity]
    result = res
    
    cap = capacity
    result_name = list()
    result_price = list()
    rez = list()
    for i in range(num_of_actions, 0, -1):
        if res <= 0:
            break
        if res == table[i - 1][cap]:
            continue
        else:
 
            result_price.append(actions[i - 1])
            result_name.append(name[i - 1])
            rez.append(benefit[i - 1])

            res = res - benefit[i - 1]
            cap = cap - actions[i - 1]

    print("Pour un total de :", sum(result_price) / 100, "€")
    print("Un bénéfice de :","%.2f" % (result / 100), "€")
    print("Un bénéfice de :","%.2f" % (sum(rez) / 100), "€")
    print("Les actions les plus rentables sont :", ', '.join(result_name))




list_actions = list()
name = list()
actions = list()
profit = list()

f = open ("dataset2_Python+P7.csv")
myReader = csv.reader(f, delimiter=',')
for col in myReader:
    if float(col[1]) > 0:
        value = (float(col[1]) * 100)
        benef = value * (float(col[2]) / 100)
        name.append(col[0])
        actions.append(int(value))
        profit.append(int(benef)) # revoir je pense


cap = 50000
capacity = cap
num_of_actions = len(actions)


knapSack(capacity, actions, profit, num_of_actions, name)
print("--- %.2f seconds ---" % (time.time() - start_time))
