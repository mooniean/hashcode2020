import numpy as np
import os

path_data = os.path.join("datasets", "c_medium.in")  # CHECK

with open(path_data) as f:
    lines = f.readlines()
    target, pizza_count = lines[0].split()
    pizzas = np.asarray(lines[1].split(), int)
    print(target, pizza_count, pizzas)

max_total = np.sum(pizzas)

for index, p in enumerate(pizzas):
    if p == target:
        print(f'Solution found at {index}')
    if p > int(target):
        np.delete(pizzas, p)

diff = max_total - int(target)
arr = []
for i in range(0, int(pizza_count), -1):
    if pizzas[pizza_count] == diff:
        print(f'Solution found at {pizza_count}')


def find_diff(array, t, start, p=None, found=False):
    if p is None:
        p = []
    if not found:
        for i in range(start, 0, -1):
            sub_diff = t - array[i]
            if sub_diff == 0:
                found = True
                find_diff(array=array, start=0, t=t, p=p+[i], found=found)
                return array, t, p
            elif t > sub_diff > 0:
                find_diff(array=array, start=i-1, t=sub_diff, p=p+[i], found=found)
            else:
                find_diff(array=array, start=i-2, t=t, p=p[0:-1], found=found)
    else:
        print(f'Solution found with: {p}')
        print(sum([array[p] for p in p]))
    return array, t, p


print(find_diff(pizzas, int(target), len(pizzas)-1))
