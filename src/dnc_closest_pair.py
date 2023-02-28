import numpy as np
from array_of_points import*
from point import*
from main import random_point
from bruteforce import closest_points



def dcd_closest_pair(arr_of_points, dimension):
    size = len(arr_of_points)

    if size <= 3:
        min_dist = np.inf
        closest_points = []
        for i in range(size - 1):
            for j in range(i+1, size):
                min_dist, closest_points = get_min_dist(min_dist, closest_points, arr_of_points[i], arr_of_points[j])
        
        return min_dist, closest_points
    
    arr_of_points = np.asarray(arr_of_points)
    arr_of_points = arr_of_points[arr_of_points[:,0].argsort(kind='mergesort')]
    x_median = arr_of_points[size//2][0]

    # print(arr_of_points)
    
    left_points, right_points = sorted_arr_divider(arr_of_points)

    left_min_dist, left_closest_points  = dcd_closest_pair(left_points, dimension)
    right_min_dist, right_closest_points= dcd_closest_pair(right_points, dimension)

    min_dist, closest_points = get_min_dist_from_2(left_min_dist, left_closest_points, right_min_dist, right_closest_points)

    left_hp = get_points_in_hyperplane(left_points, x_median, min_dist, lambda a, b: a < b)
    right_hp = get_points_in_hyperplane(right_points, x_median, min_dist, lambda a, b: a <= b)

    return get_closest_in_hyperplane(left_hp, right_hp, min_dist, dimension, closest_points)



        

    








# a = [[0, 1, 1], [0, 1, 2], [3, 2, 4], [0, 1, 6], [0, 2, 3], [1, 2, 3], [4, 3, 2]]
for i in range(100):
    a = random_point()

    q, w, e, r, t = closest_points(a)
    min_dist, arr = dcd_closest_pair(a, 3);
    if (t != min_dist):
        print(t)
        print(min_dist)
        break

# print(t)
# print(min_dist)
# print(arr)