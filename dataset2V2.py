import csv
import time
import math

start_time = time.time()
# based solution for 0-1 Knapsack problem
# Prints the items which are put in a
# knapsack of capacity W
def knapSack(capacity, actions, benefit, num_of_actions, name):
    table = [[0 for w in range(capacity + 1)]for i in range(num_of_actions + 1)]
    # Build table table[][] in bottom
    # up manner
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
 
    # stores the result of Knapsack
    res = table[num_of_actions][capacity]
    result = res
    
    cap = capacity
    result_name = list()
    result_price = list()
    gg = list()
    for i in range(num_of_actions, 0, -1):
        if res <= 0:
            break
        # either the result comes from the
        # top (table[i-1][w]) or from (benefit[i-1]
        # + table[i-1] [w-actions[i-1]]) as in Knapsack
        # table. If it comes from the latter
        # one/ it means the item is included.
        print(res == table[i - 1][cap])
        if res == table[i - 1][cap]:
            continue
        else:
 
            # This item is included.
            result_price.append(actions[i - 1])
            result_name.append(name[i - 1])
            gg.append(benefit[i - 1])

            # Since this weight is included
            # its value is deducted
            res = res - benefit[i - 1]
            cap = cap - actions[i - 1]
    

    print("Pour un total de :", sum(result_price) / 100, "€")
    print("Un bénéfice de :","%.2f" % (result / 100), "€")
    print("Un bénéfice de :","%.2f" % (sum(gg) / 100), "€")
    print("Les actions les plus rentables sont :", ', '.join(result_name))




list_actions = list()
name = list()
actions = list()
profit = list()

f = open ("dataset2_Python+P7.csv")
myReader = csv.reader(f, delimiter=',')
for col in myReader:
    if float(col[1]) > 0:
        v = float(col[1])
        p = float(col[2])
        value = (v * 100)
        benef = value * (p / 100)
        name.append(col[0])
        actions.append(int(value))
        profit.append(int(benef))
"""print(profit[0],int(profit[0]))
print(profit[1],int(profit[1]))
print(profit[2],int(profit[2]))
print(profit[3],int(profit[3]))"""

cap = 50000
capacity = cap
num_of_actions = len(actions)


knapSack(capacity, actions, profit, num_of_actions, name)
print("--- %.2f seconds ---" % (time.time() - start_time))
