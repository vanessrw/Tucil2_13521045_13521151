import math

from sympy import closest_points
from array_of_points import get_min_dist

def jarak(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2)

def brute_force_closest_pair(points, n):
    min_dist = float('inf')
    closest_p1, closest_p2 = None, None
    
    arrPoints1 = []
    arrPoints2 = []
    for i in range(n):
        for j in range(i+1, n):
            dist = jarak(points[i], points[j])
            if dist < min_dist:
                min_dist = dist
                closest_p1, closest_p2 = points[i], points[j]
                arrPoints1.append(closest_p1)
                arrPoints2.append(closest_p2)
            elif dist == min_dist:
                closest_p1, closest_p2 = points[i], points[j]
                arrPoints1.append(closest_p1)
                arrPoints2.append(closest_p2)
        closest_points = closest_p1 + closest_p2  
    
    return min_dist, closest_points