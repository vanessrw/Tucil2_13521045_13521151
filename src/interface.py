def get_int_input():
    while True:
        num = input("Masukan: ")
        try:
            val = int(num)
            return val
        except ValueError:
            try:
                float(num)
                print("\nMasukan tidak boleh bilangan desimal")
                print("Silahkan ulangi kembali")
            except ValueError:
                print("\nMasukan harus berupa bilangan bulat")
                print("Silahkan ulangi kembali")

def get_dimension_and_n():
    while True:
        print("Masukan dimensi titik")
        dimension = get_int_input()
        if dimension >= 1:
            break
        print("\nDimensi harus bernilai lebih dari sama dengan 3")

    print("")

    while True:
        print("Masukan jumlah titik")
        points_count = get_int_input()
        if points_count >= 2:
            break
        print("\nDimensi harus bernilai lebih dari sama dengan 2")

    return dimension, points_count

def output_format(time, min_distance, euclidean_count, solution_array):
    print(f"Waktu dibutuhkan                    : {time}")
    print(f"Jarak titik terdekat                : {min_distance}")
    print(f"Operasi euclidean distance sebanyak : {euclidean_count}")
    print("Pasangan titik:")
    for i in range(len(solution_array)):
        print(solution_array[i])

    