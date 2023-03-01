import numpy as np
from array_of_points import sorted_arr_divider, get_min_dist_from_2, get_points_near_hyperplane, get_closest_near_hyperplane
from brute_force import brute_force_closest_pair

def dnc_closest_pair(arr_points):
    size = len(arr_points)

    # Base case, if only 3 points or less, just use brute force approach
    if size <= 3:
        return brute_force_closest_pair(arr_points)
    
    # Divide array of points, according to x axis, less than median go to left array
    # more than median go to right array
    left_points, right_points = sorted_arr_divider(arr_points)

    # Recursively vall divide and conquer algorithm to solver for each sides
    left_min_dist, left_closest_points  = dnc_closest_pair(left_points)
    right_min_dist, right_closest_points= dnc_closest_pair(right_points)

    # Compare result for each sides and get the minimum distance and the corresponding pairs of point
    min_dist, closest_points = get_min_dist_from_2(left_min_dist, left_closest_points, right_min_dist, right_closest_points)

    # Get median to determine x axis of hyperplane
    x_median = arr_points[size//2][0]

    # Get points that at most minimum_distance near hyperplane
    left_hp, right_hp = get_points_near_hyperplane(arr_points, x_median, min_dist)

    # Compare current min_dist to the minimum distance from points near hyperplane
    min_dist, array_of_closest = get_closest_near_hyperplane(left_hp, right_hp, min_dist, closest_points)

    return min_dist, array_of_closest