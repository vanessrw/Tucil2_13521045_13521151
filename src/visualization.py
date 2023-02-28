import math
import random
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def visualization(points, arrPoints):

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    selected_points = []
    other_points = []
    for point in points:
        if point not in arrPoints:
            other_points.append(point)
    #for point in arrPoints:
        #selected_points.append(point)
    #print("points: ")
    #print(points)
    #print("arr points: ")
    #print(arrPoints)

    arrPoints3D = []
    for i in range(0, len(arrPoints), 3):
        point = [arrPoints[i], arrPoints[i+1], arrPoints[i+2]]
        arrPoints3D.append(point)
    x_coords_selected = []
    y_coords_selected = []
    z_coords_selected = []

    arrPoints3D = []
# Iterate over arrPoints in steps of 3
    for i in range(0, len(arrPoints), 3):
    # Use a list comprehension to create a 3D point from the next three elements in arrPoints
        point = [arrPoints[i], arrPoints[i+1], arrPoints[i+2]]
    # Add the point to the list of points
        arrPoints3D.append(point)

    #print(arrPoints3D)

    for point in arrPoints3D:
        if isinstance(point, (list, tuple)) and len(point) >= 3:
            x_coords_selected.append(point[0])
            y_coords_selected.append(point[1])
            z_coords_selected.append(point[2])
    #print(x_coords_selected, y_coords_selected, z_coords_selected)
    #x_coords_selected = [point[0] for point in arrPoints if isinstance(point, (list, tuple)) and len(point) >= 3]
    #y_coords_selected = [point[1] for point in arrPoints if isinstance(point, (list, tuple)) and len(point) >= 3]
    #z_coords_selected = [point[2] for point in arrPoints if isinstance(point, (list, tuple)) and len(point) >= 3]

    x_coords_other = [point[0] for point in other_points if isinstance(point, (list, tuple)) and len(point) >= 3]
    y_coords_other = [point[1] for point in other_points if isinstance(point, (list, tuple)) and len(point) >= 3]
    z_coords_other = [point[2] for point in other_points if isinstance(point, (list, tuple)) and len(point) >= 3]

    ax.scatter(x_coords_other, y_coords_other, z_coords_other, c='black')
    ax.scatter(x_coords_selected, y_coords_selected, z_coords_selected, c='red')

    ax.set_title("Scatter Plot of {} Random Points in 3D".format(len(points)))
    ax.set_xlabel("X Coordinates")
    ax.set_ylabel("Y Coordinates")
    ax.set_zlabel("Z Coordinates")

    # Display the plot
    plt.show()