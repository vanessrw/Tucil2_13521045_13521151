import math
import random
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def distance3D(p1, p2):
    # jarak 2 titik di 3D
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2 + (p2[2] - p1[2])**2)

def closest_pair(points):

    # jarak terdekat dua titik di ruang 3D. Divide and Conquer
    n = len(points)
    if n <= 3:
        # Jika titik <= 3, Brute Force untuk menghitung jarak
        min_distance = float('inf')
        for i in range(n):
            for j in range(i+1, n):
                dist = distance3D(points[i], points[j])
                if dist < min_distance:
                    min_distance = dist
        return min_distance
    
    # sort berdasarkan x
    points_sorted = sorted(points, key=lambda x: x[0])
    
    # Bagi titik jd dua bagian
    mid = n // 2
    left_points = points_sorted[:mid]
    right_points = points_sorted[mid:]
    
    # Rekursi kedua bagian 
    left_min_distance = closest_pair(left_points)
    right_min_distance = closest_pair(right_points)
    
    # Ambil jarak terkecil dari dua rekursi
    min_distance = min(left_min_distance, right_min_distance)
    
    # Cari pasangan titik yang dkt pivot, batas jarak delta
    middle_points = []
    for point in points:
        if abs(point[0] - points[mid][0]) < min_distance:
            middle_points.append(point)
    
    # sort titik berdasarkan koordinat y
    middle_points_sorted = sorted(middle_points, key=lambda x: x[1])
    
    # jarak antara setiap pasangan titik diantara dua bagian dalam suatu jendela selebar 2 * min_distance
    k = len(middle_points_sorted)
    for i in range(k):
        for j in range(i+1, k):
            if middle_points_sorted[j][1] - middle_points_sorted[i][1] >= min_distance:
                break
            dist = distance3D(middle_points_sorted[i], middle_points_sorted[j])
            if dist < min_distance:
                min_distance = dist
    
    return min_distance
    #print(min_distance)

    # randomizer 3D
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

a = random_point()
#print(len(a))
closest_pair(a)
