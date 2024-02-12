import time
from txt_input_output import *
from movement import *
from util import *

print("Jenis Input")
print("1. File .txt")
print("2. CLI")
user_input = input("Masukkan jenis input: ")

while user_input not in ["1", "2"]:
    print("Input tidak valid")
    user_input = input("Masukkan jenis input: ")

print()

if user_input == "1":
    buffer_size, matrix_size, matrix, num_sequences, sequences, points = read_file()

elif user_input == "2":
    num_unique_tokens = int(input("Masukkan jumlah token unik: "))
    unique_tokens = input("Masukkan token unik: ").split()
    buffer_size = int(input("Masukkan panjang buffer: "))
    matrix_size = tuple(map(int, input("Masukkan ukuran matriks: ").split()))
    num_sequences = int(input("Masukkan jumlah sequence: "))
    max_sequence_length = int(input("Masukkan panjang maksimal sequence: "))
    
    matrix = generate_matrix(unique_tokens, matrix_size[0], matrix_size[1])
    sequences = generate_sequences(unique_tokens, num_sequences, max_sequence_length)
    points = point_generator(num_sequences)

    print("MATRIKS:")
    for row in range(matrix_size[0]):
        for col in range(matrix_size[1]):
            print(matrix[row][col], end=" ")
        print()

start = time.time()
    
# print("Buffer Length:",  buffer_size)
# print("Matrix Size:", matrix_size)
# print("Matrix:")
# for row in matrix:
#     print(row)
# print("Number of Sequences:", num_sequences)
# print("Sequences:", sequences)
# print("Points:", points)

hor_res, hor_p = horizontal_first(sequences, num_sequences, matrix_size, matrix, points, buffer_size)
ver_res, ver_p = vertical_first(sequences, num_sequences, matrix_size, matrix, points, buffer_size)

end = time.time()

print()

if ver_res != [] and hor_res != []:
    if ver_p > hor_p:
        print_result(ver_res, ver_p)
        result = ver_res
        point = ver_p
    else:
        print_result(hor_res, hor_p)
        result = hor_res
        point = hor_p

elif ver_res != []:
    print_result(ver_res, ver_p)
    result = ver_res
    point = ver_p

elif hor_res != []:
    print_result(hor_res, hor_p)
    result = hor_res
    point = hor_p

else:
    print("Point: 0")
    print("Tidak ada sequence yang ditemukan")

print()
print("Waktu eksekusi:", (end - start)*1000, "ms")
print()
user_input2 = input("Apakah Anda ingin menyimpan solusi ke dalam file? (y/n): ").lower()

if user_input2 == "y":
    if user_input == "1":
        write_file1(result, point)
    elif user_input == "2":
        write_file2(result, point, matrix)
else:
    print("Terima kasih telah menggunakan program ini! :D")