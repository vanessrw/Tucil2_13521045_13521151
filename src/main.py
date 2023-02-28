from interface import get_dimension_and_n, output_format
from array_of_points import get_random_points
from brute_force import brute_force_closest_pair
from divide_conquer import*
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
    bf_min_distance, bf_solution_pairs = brute_force_closest_pair(arr_points, n)
    time_finish = time.time()
    bf_time = time_finish - time_start

    # Output answer brute force
    print("Dengan pendekatan brute force:")
    output_format(bf_time, bf_min_distance, bf_solution_pairs)


    # Find closest pair with divide and conquer
    time_start = time.time()


    dnc_min_distance, dnc_solution_pairs = dcd_closest_pair(arr_points, dimension)
    time_finish = time.time()
    dnc_time = time_finish - time_start

    # Output answer divide and conquer
    print("\nDengan pendekatan divide and conquer")
    output_format(dnc_time, dnc_min_distance, dnc_solution_pairs)

    if dimension == 3:
        visualization(arr_points, bf_solution_pairs)


if __name__ == '__main__':
    main()

# a = random_point()
# #print(len(a))
# closest_pair(a)
