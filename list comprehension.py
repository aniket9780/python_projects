import random
new_list = [random.randint(0,20) for x in range(20)]
print(new_list)

ini_list = [[1, 2, 3],[3, 6, 7],[7, 5, 4]]

flatten_list = [x for j in ini_list for x in j]
print(flatten_list)
