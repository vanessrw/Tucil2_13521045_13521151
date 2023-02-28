from array_of_points import get_min_dist

def brute_force_closest_pair(arr_of_points, size):
    # Initialize variable
    min_dist = float('inf')
    closest_points = []

    # Iterate all possible pair combination
    for i in range(size - 1):
        for j in range(i+1, size):
            min_dist, closest_points = get_min_dist(min_dist, closest_points, arr_of_points[i], arr_of_points[j])
    
    return min_dist, closest_points