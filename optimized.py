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

start_time = time.time()
name = list()
action_value = list()  #    wts
benefit = list() #vals
capacity = 50000

for i in range(len(actions)):
    n, v, p = actions[i]
    benef = int(v * p)
    benefit.append(benef)
    name.append(n)
    action_value.append(v)

max_value = capacity + 1  # w
num_of_actions = len(action_value)  #   h
table = [[0 for i in range(max_value)] for elem in range(num_of_actions)]

for index in range(len(benefit)):

    for value in range(max_value):
        # if the item value more than the capacity at that column?
        if action_value[index] > value:
            table[index][value] = table[index - 1][value]

            continue
        
        # if the value of the item < capacity
        prior_value = table[index - 1][value]
        #                 benefit of current item  + val of remaining value
        new_option_best = benefit[index] + table[index - 1][value - action_value[index]]
        table[index][value] = max(prior_value, new_option_best)
        #actions_name = 

print(prior_value,"priior")
print(table[index][value],'table')
result = max([x for y in table for x in y])
print(result)
print("--- %s seconds ---" % (time.time() - start_time))