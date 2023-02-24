import math
import random

def jarak(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2)

def closest_points(points):
    n = len(points)
    min_dist = float('inf')
    closest_p1, closest_p2 = None, None
    
    for i in range(n):
        for j in range(i+1, n):
            dist = jarak(points[i], points[j])
            if dist < min_dist:
                min_dist = dist
                closest_p1, closest_p2 = points[i], points[j]
    
    return closest_p1, closest_p2, min_dist

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

points = random_point()
closest_p1, closest_p2, min_dist = closest_points(points)
print("Titik terdekat: ", closest_p1, "dan", closest_p2, "dengan jarak", min_dist)
