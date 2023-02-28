import math
import random
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sympy import false, true

def jarak(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2)

def tuple_pair_points(arrpoint1, arrpoint2):
    pairs = [(arrpoint1[i], arrpoint2[i]) for i in range (len(arrPoints1))]
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

def compare_point(point1, point2):
    i = 0
    equal = true
    while i < len(point1) and equal:
        if point1[i] != point2[i]:
            equal = false
        i+=1

    return equal
#print("Titik terdekat : ", closest_p1, "dan", closest_p2)
#print("dengan jarak", min_dist)

points = random_point()
arrPoints1, arrPoints2, closest_p1, closest_p2, min_dist = closest_points(points)

for i in range(len(arrPoints1)):
    print("Titik terdekat ", i+1, ": ", arrPoints1[i], "dan", arrPoints2[i])
    print("dengan jarak", min_dist)

#def isClose(point):
#    arrPointsFin = np.concatenate((arrPoints1, arrPoints2))
#    is_in_array = np.isin(points, arrPointsFin).all(axis=1).any()
#    return is_in_array

def visualization(points):
    # Extract x, y, and z coordinates from the array of points
    x_coords = [point[0] for point in points]
    y_coords = [point[1] for point in points]
    z_coords = [point[2] for point in points]

    # Define the indices of the points to differentiate
    #indices_to_differentiate = []
    #for point in points:
    #    if isClose(point):
    #        indices_to_differentiate.append(point)


    # Create a 3D scatter plot of the points
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    #ax.scatter(x_coords, y_coords, z_coords)

    #coloring
    #if isClose(points):
    #    ax.scatter(x_coords, y_coords, z_coords, color='red')
    #for point in points:
    #    if np.isin(point, arrPoints1).any() or np.isin(point, arrPoints2).any():
    #        ax.scatter(x_coords, y_coords, z_coords, color='black')
    #    else:
    #        ax.scatter(x_coords, y_coords, z_coords, color='red')

    selected_points = []
    other_points = []
    for point in points:
        if point in arrPoints1:
            #ax.scatter(x_coords, y_coords, z_coords, c='red')
            selected_points.append(point) 
            #print('in arr1')
        if point in arrPoints2:
        #if compare_point(point, arrPoints1):
            #ax.scatter(x_coords, y_coords, z_coords, c='red')
            selected_points.append(point)
            #print('in arr2')
        else:
            other_points.append(point)
            #ax.scatter(x_coords, y_coords, z_coords, c='blue')
    x_coords_selected = [point[0] for point in selected_points]
    y_coords_selected = [point[1] for point in selected_points]
    z_coords_selected = [point[2] for point in selected_points]

    x_coords_other = [point[0] for point in other_points]
    y_coords_other = [point[1] for point in other_points]
    z_coords_other = [point[2] for point in other_points]

    ax.scatter(x_coords_other, y_coords_other, z_coords_other, c='black')
    ax.scatter(x_coords_selected, y_coords_selected, z_coords_selected, color='red')



        #if not isClose(point):
        #    ax.scatter(x_coords, y_coords, z_coords, color='black')
        #if isClose(point):
        #    ax.scatter(x_coords, y_coords, z_coords, color='red')

    # Set the title and axis labels
    ax.set_title("Scatter Plot of {} Random Points in 3D".format(len(points)))
    ax.set_xlabel("X Coordinates")
    ax.set_ylabel("Y Coordinates")
    ax.set_zlabel("Z Coordinates")

    # Display the plot
    plt.show()


print(tuple_pair_points(arrPoints1, arrPoints2))
visualization(points)
#visualization_target(arrPoints1, arrPoints2)