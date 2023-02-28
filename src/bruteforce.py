import math
import random
from visualization import*
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sympy import false, true

def jarak(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2)

def tuple_pair_points(arrpoint1, arrpoint2):
    pairs = [(arrpoint1[i], arrpoint2[i]) for i in range (len(arrpoint1))]
    return pairs

def closest_points(points):
    n = len(points)
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
    
    return arrPoints1, arrPoints2, closest_p1, closest_p2, min_dist

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


#points = random_point()
#arrPoints1, arrPoints2, closest_p1, closest_p2, min_dist = closest_points(points)
#arrPoints = arrPoints1 + arrPoints2

#for i in range(len(arrPoints1)):
    #print("Titik terdekat ", i+1, ": ", arrPoints1[i], "dan", arrPoints2[i])
    #print("dengan jarak", min_dist)

#print(min_dist)
#visualization(points, arrPoints)