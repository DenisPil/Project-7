import time
import csv


actions = list()
benefit = list()
f= open ("actions_premiere_partie.csv")
myReader = csv.reader(f)
for row in myReader:
    actions.append(row)
del actions[0]

start_time = time.time()
name = list()
action_value = list()  #    wts
benefit = list() #vals
capacity = 50000

for i in range(len(actions)):
    n, v, p = actions[i]
    value = int(v) * 100
    benef = value * (int(p) / 100)
    benefit.append(benef)
    name.append(n)
    action_value.append(value)



max_value = capacity + 1  # w
num_of_actions = len(action_value)  #   h
table = [[0 for i in range(max_value)] for elem in range(num_of_actions)]

for index in range(len(benefit)):

    for value in range(max_value):

        if action_value[index] > value:
            table[index][value] = table[index - 1][value]
            continue

        prior_value = table[index - 1][value]
        new_option_best = benefit[index] + table[index - 1][value - action_value[index]]
        table[index][value] = max(prior_value, new_option_best)
        #print ("\n\n\n" "\nbenefit[index] :", benefit[index], "\n+","\ntable[index - 1] :","trop long", "\n\nvalue :",value, "\n-", "\naction_value[index] : ",action_value[index],"\nvalue - action_value[index] :", value - action_value[index],"\n=" "new_option_best :",new_option_best)


result = max([x for y in table for x in y])
print(result)
print("--- %s seconds ---" % (time.time() - start_time)) 

"""         poid   benef   Pmax =   0  1  2  3  4  5 

     A         1       1           [0, 1, 1, 1, 1, 1] 
     B         3       4           [0, 1, 1, 4, 5, 5]
     C         4       5           [0, 1, 1, 4, 5, 6] 
     D         5       7           [0, 1, 1, 4, 5, 7]
"""""