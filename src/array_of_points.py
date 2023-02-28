import numpy as np
from point import is_projection_close, euclidean_distance, is_close_hyperplane

def get_min_dist(min_dist, array_of_closest, point_1, point_2):
    test_dist = euclidean_distance(point_1, point_2)
    if test_dist < min_dist:
        min_dist = test_dist
        array_of_closest = [[point_1, point_2]]
    elif test_dist == min_dist:
        array_of_closest.append([point_1, point_2])

    return min_dist, array_of_closest

def get_min_dist_from_2(min_dist_1, closest_point_1, min_dist_2, closest_point_2):
    if min_dist_1 < min_dist_2:
        min_dist = min_dist_1
        closest_points = closest_point_1
    elif min_dist_2 < min_dist_1:
        min_dist = min_dist_2
        closest_points = closest_point_2
    else:
        min_dist = min_dist_1
        closest_points = closest_point_1
        closest_points.extend(closest_point_2)
    
    return min_dist, closest_points

def sorted_arr_divider(sorted_arr):
    size = np.shape(sorted_arr)[0]
    under_median = []
    over_median = []

    for i in range(size // 2):
        under_median.append(sorted_arr[i])

    for i in range(size // 2, size):
        over_median.append(sorted_arr[i])

    under_median = np.asarray(under_median)
    over_median = np.asarray(over_median)

    return (under_median, over_median)

def unsorted_arr_divider(arr, median, axis):
    size = np.shape(arr)[0]

    under_median = []
    over_median = []

    for i in range(size):
        if arr[i][axis] < median:
            under_median.append(arr[i])
        else:
            over_median.append(arr[i])
            
    return(under_median, over_median)

def get_points_in_hyperplane(points, hp_axis, delta, func):
    size = len(points)
    left_hp = []
    right_hp = []
    in_hyperplane = []

    # for i in range(size):
    #     if is_close_hyperplane(points[i], hp_axis, delta, lambda a, b: a < b):
    #         left_hp.append(points[i])
    #     elif is_close_hyperplane(points[i], hp_axis, delta, lambda a, b: a >= b)

    for i in range(size):
        if (func(abs(hp_axis - points[i][0]), delta)):
            in_hyperplane.append(points[i])

    # if (is_left):
    #     for i in range(size):
    #         if (hp_axis - points[i][0] < delta):
    #             in_hyperplane.append(points)
    #         else:
    #             continue
    
    # else:
    #     for i in range(size):
    #         if (points[i][0] - hp_axis <= delta):
    #             in_hyperplane.append(points)
    #         else:
    #             break

    return np.asarray(in_hyperplane)

def get_closest_in_hyperplane(left_arr, right_arr, delta, dimension, array_of_closest):
    min_dist = delta
    size_left = left_arr.shape[0]
    size_right = right_arr.shape[0]
    for i in range(size_left):
        for j in range(size_right):

            if is_projection_close(left_arr[i], right_arr[j], delta, dimension):

                min_dist, array_of_closest = get_min_dist(min_dist, array_of_closest, left_arr[i], right_arr[j])


    return min_dist, array_of_closest

# a = [[1,10],[3,8],[5,9]]
# # b = [[3,8],[5,9],[1,10]]

# x, y = sorted_arr_divider(a)
# # x, y = unsorted_arr_divider(b, 3, 0)

# print(x)
# print(y)