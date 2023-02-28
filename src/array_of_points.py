import numpy as np
import random
from point import is_projection_close, euclidean_distance

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

    return (under_median, over_median)

def get_points_in_hyperplane(points, hp_axis, delta):
    size = len(points)
    left_hp = []
    right_hp = []
    in_hyperplane = []

    for i in range(size):
        if hp_axis - delta <= points[i][0] < hp_axis:
            left_hp.append(points[i])
        elif hp_axis <= points[i][0] <= hp_axis + delta:
            right_hp.append(points[i])

    # for i in range(size):
    #     if (func(abs(hp_axis - points[i][0]), delta)):
    #         in_hyperplane.append(points[i])

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

    return left_hp, right_hp

def get_closest_in_hyperplane(left_arr, right_arr, min_dist, dimension, array_of_closest):
    size_left = len(left_arr)
    size_right = len(right_arr)
    for i in range(size_left):
        for j in range(size_right):

            if is_projection_close(left_arr[i], right_arr[j], min_dist, dimension):

                min_dist, array_of_closest = get_min_dist(min_dist, array_of_closest, left_arr[i], right_arr[j])


    return min_dist, array_of_closest

def get_random_points(dimension, count):
    points = []
    for i in range(count):
        point = []
        for j in range(dimension):
            coordinate = random.uniform(-100, 100)
            rounded_coordinate = round(coordinate, 2)
            point.append(rounded_coordinate)
        points.append(point)
    return points

# a = [[1,10],[3,8],[5,9]]
# # b = [[3,8],[5,9],[1,10]]

# x, y = sorted_arr_divider(a)
# # x, y = unsorted_arr_divider(b, 3, 0)

# print(x)
# print(y)