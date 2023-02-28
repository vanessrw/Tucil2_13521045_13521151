import numpy as np

# count_euclidean_distance = 0;

def euclidean_distance(point_1, point_2):
    # count_euclidean_distance += 1
    point_1 = np.asarray(point_1)
    point_2 = np.asarray(point_2)
    difference_res = np.subtract(point_1, point_2)
    squared_res = np.power(difference_res, 2)
    sum_res = np.sum(squared_res)
    return np.sqrt(sum_res)

def is_close_hyperplane(point, hp_axis, threshold, func):
    return func(point[0] - hp_axis, threshold)
    

def is_projection_close(point_1, point_2, delta, dimesion) -> bool:
    for i in range(1, dimesion):
        if (abs(point_1[i] - point_2[i]) > delta):
            return False
        
    return True




# print(euclidean_distance([1,1], [2,2]))