#Note, this was a very ineffective solution to graph searchin/ traveling saleman problems. It does work, but not well, so it is not recomended to use as an example.. maybe as an example of what not to do.. Also this was done in a group project so I don't take full credit for this.

from salesmap import *
import numpy as np
n = 15
name = 'map'+str(n)+'.npy'
sm = SalesMap(name)
#path = list(range(n))+[0]
#for item in sm.coordinates:
#    print(item) 
#print(sm.loss(path))
#sm.show(path)

coords_list = sm.coordinates.tolist()
coords_zero = [0] * len(coords_list)
path_list = [0]
path_length_list = []
def find_path(point):
    if coords_list != coords_zero:
        print(coords_list.index(point))
        dist_list = dict()
        count = 0
        for val in coords_list:
            dist_list[count] = sm.loss([coords_list.index(val),coords_list.index(point)])
            count += 1
        smallest = 1
        coords_list[coords_list.index(point)] = 0
        dist_list_copy = dict(dist_list)
        for key, value in dist_list_copy.items():
            if value == 0:
                del dist_list[key]
        for key, value in dist_list.items():
            if value < smallest and value != 0.0:
                smallest = value
                smallest_key = key
        print(dist_list)
        print(smallest)
        print(coords_list)
        print('Run complete.')
        path_length_list.append(smallest)
        path_list.append(smallest_key)
        return find_path(coords_list[smallest_key])
    else:
        return
find_path(coords_list[0])
length = 0.0
for val in path_length_list:
    length += val
path_list.append(0)
print(path_list)
print(length)
sm.show(path_list)
