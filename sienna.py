import time
import csv


start_time = time.time()
list_actions = list()
name = list()
actions = list()  #    wts
profit = list() #vals

f = open ("dataset2_Python+P7.csv")
myReader = csv.reader(f)
for row in myReader:
    list_actions.append(row)
del list_actions[0]

for i in range(len(list_actions)):
    n, v, p = list_actions[i]

    if float(v) > 0:
        value = (float(v) * 100)
        benef = value * (float(p) / 100)
        profit.append(benef)
        name.append(n)
        actions.append(int(value))


cap = 50000
capacity = cap + 1
num_of_actions = len(actions)

table = [[0 for i in range(capacity)] for elem in range(num_of_actions)]
index = [["" for i in range(capacity)] for elem in range(num_of_actions)]
for row in range(len(actions)):
    for column in range(capacity):
        
     
        if actions[row] > column:
            table[row][column] = table[row - 1][column]
            index[row][column] = index[row - 1][column]
 
            continue
        prior_value = table[row - 1][column]
        new_option_best = profit[row] + table[row - 1][column - actions[row]]

        prior_index = index[row - 1][column]
        best_index = index[row - 1][column - actions[row]]
        new_index_best = str(row) + " " + str(best_index)

        if prior_value < new_option_best :
            table[row][column] = new_option_best
            index[row][column] = new_index_best
        else:
            table[row][column] = prior_value
            index[row][column] = prior_index

print(max(prior_value, new_option_best))        
result = max([x for y in table for x in y])
len_index = len(index) - 1
rez = index[len_index][-1].split()

result_name = list()
result_price = list()
for i in rez:
    elem = int(i)
    result_name.append(name[elem])
    result_price.append(actions[elem])

print("Pour un total de :", sum(result_price) / 100, "€")
print("Les actions les plus rentables sont :", ', '.join(result_name))
print("Pour un bénéfice de :","%.2f" % (result / 100), "€" )
print("--- %s seconds ---" % (time.time() - start_time))
