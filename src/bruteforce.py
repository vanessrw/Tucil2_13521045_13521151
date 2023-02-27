import math
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def jarak(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2)

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

# plot 3D
# input: array of points
def visual(points):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(points[0], points[1], points[2], c='r', marker='o')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()

points = random_point()
arrPoints1, arrPoints2, closest_p1, closest_p2, min_dist = closest_points(points)

for i in range(len(arrPoints1)):
    print("Titik terdekat ", i+1, ": ", arrPoints1[i], "dan", arrPoints2[i])
    print("dengan jarak", min_dist)

#print("Titik terdekat : ", closest_p1, "dan", closest_p2)
#print("dengan jarak", min_dist)
