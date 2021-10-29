import csv
import time


def dataset_choice():
    print("Choisir :\n 1 : dataset_1\n 2 : dataset_2\n 3 : actions première partie\n 4 : nouveau dataset :")
    dataset = input("Entrez 1, 2, 3 ou 4 : ")
    result = ""
    if dataset == "1":
        result = "dataset1_Python+P7.csv"
    if dataset == "2":
        result = "dataset2_Python+P7.csv"
    if dataset == "3":
        result = "actions_premiere_partie.csv"
    if dataset == "4":
        result = input("Nom du fichier :")
  
    return result

def knapSack(capacity, actions, benefit, num_of_actions, name):

    table = [[0 for w in range(capacity + 1)]for i in range(num_of_actions + 1)]
    names_result = list()
    prices_result = list()

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

    for i in range(num_of_actions, 0, -1):
        if res <= 0:
            break
        if res == table[i - 1][cap]:
            continue
        else:
            prices_result.append(actions[i - 1])
            names_result.append(name[i - 1])

            res = res - benefit[i - 1]
            cap = cap - actions[i - 1]

    print("Pour un total de :", sum(prices_result) / 100, "€")
    print("Un bénéfice de :","%.2f" % (result / 100), "€")
    print("Les actions les plus rentables sont :", ', '.join(names_result))


list_actions = list()
name = list()
actions = list()
profit = list()
capacity = 50000

f = open (dataset_choice())
start_time = time.time()
myreader = csv.reader(f, delimiter=',')
next(myreader)
for col in myreader:
    if float(col[1]) > 0:
        value = (float(col[1]) * 100)
        benef = value * (float(col[2]) / 100)
        name.append(col[0])
        actions.append(round(value))
        profit.append(round(benef))

num_of_actions = len(actions)

knapSack(capacity, actions, profit, num_of_actions, name)
print("--- %.2f seconds ---" % (time.time() - start_time))
