import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def visualization(points, solution_pairs):

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    for point in points:
        ax.scatter(point[0], point[1], point[2], c='black')

    for i, point in enumerate(solution_pairs):
        if (i % 3) == 0:
            ax.scatter(point[0][0], point[0][1], point[0][2], c='blue')
            ax.scatter(point[1][0], point[1][1], point[1][2], c='blue')
        elif (i % 3) == 1:
            ax.scatter(point[0][0], point[0][1], point[0][2], c='green')
            ax.scatter(point[1][0], point[1][1], point[1][2], c='green')
        else:
            ax.scatter(point[0][0], point[0][1], point[0][2], c='red')
            ax.scatter(point[1][0], point[1][1], point[1][2], c='red')

        x = [point[0][0], point[1][0]] 
        y = [point[0][1], point[1][1]] 
        z = [point[0][2], point[1][2]] 

        ax.plot(x, y, z, color='black')

    ax.set_title("Scatter Plot of {} Random Points in 3D".format(len(points)))
    ax.set_xlabel("X Coordinates")
    ax.set_ylabel("Y Coordinates")
    ax.set_zlabel("Z Coordinates")

    # Display the plot
    plt.show()