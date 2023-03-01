from interface import get_dimension_and_n, output_format
from array_of_points import get_random_points
from brute_force import brute_force_closest_pair
from quicksort import quicksort
from divide_conquer import dnc_closest_pair
from visualization import visualization
import time

def main():
    # Get input from user
    print("Selamat datang di closest pair finder")
    dimension, n = get_dimension_and_n()

    # Generate random points
    arr_points = get_random_points(dimension, n)

    # Find closest pair with brute force
    time_start = time.time()
    bf_min_distance, bf_solution_pairs = brute_force_closest_pair(arr_points)
    time_finish = time.time()

    bf_time = time_finish - time_start
    from point import euclidean_count as bf_euclidean_count

    # Output answer brute force
    print("\nDengan pendekatan brute force:")
    output_format(bf_time, bf_min_distance, bf_euclidean_count, bf_solution_pairs)


    # Find closest pair with divide and conquer
    time_start = time.time()
    arr_points = quicksort(arr_points)
    dnc_min_distance, dnc_solution_pairs = dnc_closest_pair(arr_points)
    time_finish = time.time()

    dnc_time = time_finish - time_start
    from point import euclidean_count
    dnc_euclidean_count = euclidean_count - bf_euclidean_count

    # Output answer divide and conquer
    print("\nDengan pendekatan divide and conquer")
    output_format(dnc_time, dnc_min_distance,dnc_euclidean_count, dnc_solution_pairs)

    # Get visualization if points in 3D
    if dimension == 3:
        visualization(arr_points, bf_solution_pairs)

if __name__ == '__main__':
    main()