import numpy as np
import random
from point import is_projection_close, euclidean_distance

def get_random_points(dimension, count):
    """Return array of random points, with each points have coordinate
    ranged between -100 and 100

    Args:
        dimension (int): dimension of points
        count (int): how many points to generate

    Returns:
        array of points: 
    """
    points = []
    for i in range(count):
        point = []
        for j in range(dimension):
            coordinate = random.uniform(-100, 100)
            rounded_coordinate = round(coordinate, 2)
            point.append(rounded_coordinate)
        points.append(point)
    return points

def get_min_dist(min_dist, array_of_closest, point_1, point_2):
    """Compare and get minimum distance of current min_dist
    compared between distance between two points, update
    the accumulation array accordingly

    Args:
        min_dist (real): current minimum distance
        array_of_closest (array of pair of points): accumulation array
        point_1 (array of real): 
        point_2 (array of real):

    Returns:
        tuple of minimum distance and accumulation array:
    """
    test_dist = euclidean_distance(point_1, point_2)
    if test_dist < min_dist:
        min_dist = test_dist
        array_of_closest = [[point_1, point_2]]
    elif test_dist == min_dist:
        array_of_closest.append([point_1, point_2])

    return min_dist, array_of_closest

def get_min_dist_from_2(min_dist_1, closest_point_1, min_dist_2, closest_point_2):
    """Get minimum distance from comparing two minimum distance candidate
    and two accumulation array

    Args:
        min_dist_1 (real): 
        closest_point_1 (array of pair of points): 
        min_dist_2 (real): 
        closest_point_2 (array of pair of points):

    Returns:
        tuple of minimum distance and accumulation array:
    """
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
    """I.S. input array is sorted
    divide an array to two relativly even number of element
    according to its x_axis value

    Args:
        sorted_arr (array of points): array already sorted increasing

    Returns:
        tuple of two divided array
    """
    size = np.shape(sorted_arr)[0]
    under_median = []
    over_median = []

    for i in range(size // 2):
        under_median.append(sorted_arr[i])

    for i in range(size // 2, size):
        over_median.append(sorted_arr[i])

    return (under_median, over_median)

def get_points_near_hyperplane(points, hp_axis, delta):
    """Get points that are atleast within distance of delta
    to hyperplane. Also group the array into two groups
    according to whether its left or right of hyperplane

    Args:
        points (array of points):
        hp_axis (real): hyperplane x axis value
        delta (real): minimum distance

    Returns:
        tuple of two divided array
    """
    size = len(points)
    left_hp = []
    right_hp = []

    for i in range(size):
        if hp_axis - delta <= points[i][0] < hp_axis:
            left_hp.append(points[i])
        elif hp_axis <= points[i][0] <= hp_axis + delta:
            right_hp.append(points[i])

    return left_hp, right_hp

def get_closest_near_hyperplane(left_arr, right_arr, min_dist, array_of_closest):
    """Compare current minimum distance to minimum distance found between
    pair of points near hyperplane. Update the array_of_closest as accumulation
    array accordingly

    Args:
        left_arr (_type_): _description_
        right_arr (_type_): _description_
        min_dist (_type_): _description_
        array_of_closest (_type_): _description_

    Returns:
        _type_: _description_
    """
    size_left = len(left_arr)
    size_right = len(right_arr)
    for i in range(size_left):
        for j in range(size_right):
            if is_projection_close(left_arr[i], right_arr[j], min_dist):
                min_dist, array_of_closest = get_min_dist(min_dist, array_of_closest, left_arr[i], right_arr[j])


    return min_dist, array_of_closest

