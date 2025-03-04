import numpy as np


# list_of_lists = [
#     #[1, 2, 3],
#     #[4, 5, 6], 
#     [7, 8, 9]
#     ]

# copy_of_last_list = list_of_lists[-1]

# print(copy_of_last_list)

list = [0, 0, 0, 0, 0]
len(list)
density= 0.5

for index in len(list):
    print(index)
    random_number = np.random.rand()
    print(random_number)
    if density <= random_number:
        print(index)
        list[index] = 1

print(list)