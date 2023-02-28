import numpy as np
from array_of_points import sorted_arr_divider, get_min_dist_from_2, get_points_in_hyperplane, get_closest_in_hyperplane
from brute_force import brute_force_closest_pair
import time

# global count_euclidean_distance

def dnc_closest_pair(arr_of_points, dimension):
    size = len(arr_of_points)

    if size <= 3:
        return brute_force_closest_pair(arr_of_points, size)
    
    x_median = arr_of_points[size//2][0]
    
    left_points, right_points = sorted_arr_divider(arr_of_points)

    left_min_dist, left_closest_points  = dnc_closest_pair(left_points, dimension)
    right_min_dist, right_closest_points= dnc_closest_pair(right_points, dimension)

    min_dist, closest_points = get_min_dist_from_2(left_min_dist, left_closest_points, right_min_dist, right_closest_points)

    left_hp, right_hp = get_points_in_hyperplane(arr_of_points, x_median, min_dist)

    min_dist, array_of_closest = get_closest_in_hyperplane(left_hp, right_hp, min_dist, dimension, closest_points)

    return min_dist, array_of_closest








# # a = [[0, 1, 1], [0, 1, 2], [3, 2, 4], [0, 1, 6], [0, 2, 3], [1, 2, 3], [4, 3, 2]]
# # for i in range(100):
# # count_euclidean_distance = 0;
# a = random_point(4, 10000)
# a = np.asarray(a)
# a = a[a[:,0].argsort(kind='mergesort')]
# a = a.tolist()

# # q, w, e, r, t = closest_points(a)

# time_start = time.time()
# min_dist, arr = dnc_closest_pair(a, 3);
# time_finish = time.time()

# timetaken = (time_finish - time_start)
# from point import count_euclidean_distance
# print(count_euclidean_distance)

# # arrTemp = []
# # for i in arr :
# #     temp = []
# #     for j in i :
# #         temp = temp + [j]
# #     arrTemp = arrTemp + [temp]

# print(timetaken)
# # if (t != min_dist):
# #     print(t)
# #     print(min_dist)
# #     break

# # print(t)
# print(min_dist)
# print(arr)
# # print(arrTemp)
# # print("\n")
# # print(a[0])

# # if arr[0][0]):
# #     print("HORE")


# # print(arr[0][0])
