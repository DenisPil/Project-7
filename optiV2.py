import time
               #V  Benef
actions = [
    ('action-1',1, 1),
    ('action-2',3, 4),
    ('action-3',4, 5),
    ('action-4',5, 7),]
"""('action-5',60, 0.17),
    ('action-6',80, 0.25),
    ('action-7',22, 0.07),
    ('action-8',26, 0.11),
    ('action-9',48, 0.13),
    ('action-10',34, 0.27),
    ('action-11',42, 0.17),
    ('action-12',110, 0.09),
    ('action-13',38, 0.23),
    ('action-14',14, 0.01),
    ('action-15',18, 0.03),
    ('action-16',8, 0.08),
    ('action-17',4, 0.12),
    ('action-18',10, 0.14),
    ('action-19',24, 0.21),
    ('action-20',114, 0.18)
    ]"""

start_time = time.time()

name = list()
action_value = list()  #    wts
benefit = list()       #    vals

for i in range(len(actions)):
    n, v, p = actions[i]
    benef = (v * p)
    #benefit.append(benef)
    benefit.append(p)
    name.append(n)
    action_value.append(v)

capacity = 5
max_value = capacity + 1
num_of_actions = len(action_value)

table = [[0 for i in range(max_value)] for elem in range(num_of_actions)]

gg = list()
jojo = list()
for index in range(len(action_value)):
    
    for value in range(max_value):

        if action_value[index] > value:
            table[index][value] = table[index - 1][value]
            continue
        prior_value = table[index - 1][value]
        new_option_best = benefit[index] + table[index - 1][value - action_value[index]]


        new_option_name = table[index - 1][index]

        gg.append(index)
        #print(test)
        print ("\n\n\n" "\nbenefit[index] :", benefit[index], "\n+","\ntable[index - 1] :",table[index - 1], "\n\nvalue :",value, "\n-", "\naction_value[index] : ",action_value[index],"\nvalue - action_value[index] :", value - action_value[index],"\n=" "new_option_best :",new_option_best)
        table[index][value] = max(prior_value, new_option_best)
        

result = ([x for y in table for x in y])

print("--- %s seconds ---" % (time.time() - start_time))

"""         poid   benef   Pmax =   0  1  2  3  4  5 

     A         1       1           [0, 1, 1, 1, 1, 1] 
     B         3       4           [0, 1, 1, 4, 5, 5]
     C         4       5           [0, 1, 1, 4, 5, 6] 
     D         6       7           [0, 1, 1, 4, 5, 7]
"""