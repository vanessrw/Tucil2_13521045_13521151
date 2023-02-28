import numpy as np
from array_of_points import*
from point import*
from main import random_point
from bruteforce import closest_points
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from visualization import*
import random
import array as arr

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = []
        right = []
        for i in range(1, len(arr)):
            if arr[i][0] < pivot[0]:
                left.append(arr[i])
            else:
                right.append(arr[i])
        return quicksort(left) + [pivot] + quicksort(right)


def dcd_closest_pair(arr_of_points, dimension):
    size = len(arr_of_points)

    if size <= 3:
        min_dist = np.inf
        closest_points = []
        for i in range(size - 1):
            for j in range(i+1, size):
                min_dist, closest_points = get_min_dist(min_dist, closest_points, arr_of_points[i], arr_of_points[j])
        
        return min_dist, closest_points
    
    #arr_of_points = np.asarray(arr_of_points)
    arr_of_points = quicksort(arr_of_points)
    x_median = arr_of_points[size//2][0]

    # print(arr_of_points)
    left_points, right_points = sorted_arr_divider(arr_of_points)

    left_min_dist, left_closest_points  = dcd_closest_pair(left_points, dimension)
    right_min_dist, right_closest_points= dcd_closest_pair(right_points, dimension)

    min_dist, closest_points = get_min_dist_from_2(left_min_dist, left_closest_points, right_min_dist, right_closest_points)

    left_hp = get_points_in_hyperplane(left_points, x_median, min_dist, lambda a, b: a < b)
    right_hp = get_points_in_hyperplane(right_points, x_median, min_dist, lambda a, b: a <= b)

    min_dist, array_of_closest = get_closest_in_hyperplane(left_hp, right_hp, min_dist, dimension, closest_points)

    #return get_closest_in_hyperplane(left_hp, right_hp, min_dist, dimension, closest_points)
    for i in range(len(array_of_closest)):
        for j in range(len(array_of_closest[i])):
            if isinstance(array_of_closest[i][j], np.ndarray):
                array_of_closest[i][j] = array_of_closest[i][j].tolist()

    return min_dist, array_of_closest


def random_point():
    points = []
    n = random.randint(2, 100)
    for i in range(n):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        z = random.uniform(0, 1)
        point = (x, y, z)
        points.append(point)
    return points

def tuple_to_arr(arr):
    arrPoints = []
    for i in range(len(arr)):
        arrPoints.append(arr[i][0])
        arrPoints.append(arr[i][1])
    return arrPoints

        
points = random_point()
min_dist, array_of_closest = dcd_closest_pair(points, 3)


#dcd_closest_pair(points, 3)
arrPoints = tuple_to_arr(array_of_closest)
visualization(points, arrPoints)
print("jarak terdekatnya adalah:", min_dist)
print("pasangan titik terdekat adalah:", array_of_closest)
#print(array_of_closest)
#print(len(array_of_closest))
#print(arrPoints)
#print(len(arrPoints))
#print(len(arrPoints1))