import math
import random
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def visualization(points, arrPoints):
    # Extract x, y, and z coordinates from the array of points
    x_coords = [point[0] for point in points]
    y_coords = [point[1] for point in points]
    z_coords = [point[2] for point in points]

    # Create a 3D scatter plot of the points
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    #ax.scatter(x_coords, y_coords, z_coords)

    selected_points = []
    other_points = []
    for point in points:
        if point in arrPoints:
            selected_points.append(point) 
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