import time
# A Dynamic Programming based Python 
# Program for 0-1 Knapsack problem
# Returns the maximum value that can 
# be put in a knapsack of capacity W
start_time = time.time()
gg = list()
def knapSack(capacity, actions_value, benefit, max_value):
    table = [[0 for x in range(capacity + 1)] for x in range(max_value + 1)]
  
    # Build table table[][] in bottom up manner
    for index in range(max_value + 1):
        for value in range(capacity + 1):
            if index == 0 or value == 0:
                table[index][value] = 0
            elif actions_value[index-1] <= value:
                table[index][value] = max(benefit[index-1] + table[index-1][value-actions_value[index-1]], table[index-1][value])
                print("premier print", table[index][value])
                toto = 0
                while toto != len(table):
                    toto +=1
                    #print(benefit[index] + table[index - 1][value - action_value[index]])
                    if table[index][value] ==table[index -toto][value]:

                        gg.append(index)

            else:
                table[index][value] = table[index-1][value]
                print('deuxieme print', table[index][value])
    return table[max_value][capacity]
  
# Driver program to test above function

"""         poid   benef   Pmax =   0  1  2  3  4  5 

     A         1       1           [0, 1, 1, 1, 1, 1] 
     B         3       4           [0, 1, 1, 4, 5, 5]
     C         4       5           [0, 1, 1, 4, 5, 6] 
     D         5       7           [0, 1, 1, 4, 5, 7]
"""""



actions = [
    ('action-1',1, 1),
    ('action-2',3, 4),
    ('action-3',4, 5),
    ('action-4',5, 7),]
 
"""('action-1',20, 0.05),
    ('action-2',30, 0.10),
    ('action-3',50, 0.15),
    ('action-4',70,0.2),
    ('action-5',60, 0.17),
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

name = list()
action_value = list()  #    wts
benefi = list() #vals



for index in range(len(actions)):
    nn, v, p = actions[index]
    value = int(v) * 100
    #benef = value * p 
    #benefi.append(benef)
    benefi.append(p)
    name.append(nn)
    action_value.append(v)
 
benefit = benefi
actions_value = action_value
capacity = 5
max_value = len(benefit)

print(knapSack(capacity, actions_value, benefit, max_value))
print(gg)
print("--- %s seconds ---" % (time.time() - start_time))