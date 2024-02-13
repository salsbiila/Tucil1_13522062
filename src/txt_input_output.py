import os
from util import *

def read_file():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    input_file = input("Masukkan nama file: ")
    input_file = os.path.join(current_directory, '..', 'test', f'{input_file}')

    while not os.path.exists(input_file):
        print("File tidak ditemukan")
        input_file = input("Masukkan nama file: ")
        input_file = os.path.join(current_directory, '..', 'test', f'{input_file}')

    buffer_size = 0
    matrix_size = (0, 0)
    matrix = []
    num_sequences = 0
    sequences = []
    points = []

    with open(input_file, "r") as file:
        lines = file.readlines()
        for line_index, line in enumerate(lines):
            line = line.strip()
            if not line:
                continue
            tokens = line.split()

            if line_index == 0:
                buffer_size = int(tokens[0])

            elif line_index == 1:
                matrix_size = (int(tokens[0]), int(tokens[1]))

            elif 1 < line_index <= matrix_size[0] + 1:
                matrix.append(tokens)

            elif line_index == matrix_size[0] + 2:
                num_sequences = int(tokens[0])

            elif matrix_size[0] + 3 <= line_index < matrix_size[0] + 3 + num_sequences * 2:
                if (line_index - matrix_size[0] - 3) % 2 == 0:
                    sequences.append(tokens)
                else:
                    points.append(tokens[0])

    return buffer_size, matrix_size, matrix, num_sequences, sequences, points

def write_file1(result, point):
    folder_path = os.path.join(os.path.abspath('.'), 'test')
    file_name = input("Masukkan nama file (.txt): ")
    file_path = os.path.join(folder_path, f'{file_name}')

    while os.path.exists(file_path):
        overwrite = input("File dengan nama tersebut sudah ada. Apakah Anda ingin melakukan overwrite? (y/n): ").lower()
        if overwrite != 'y':
            file_name = input("Masukkan nama file (.txt): ")
            file_path = os.path.join(folder_path, f'{file_name}')
        else:
            break
    
    sequence = sequence_string(result)
    coordinate = coordinate_string(result)

    with open(file_path, 'w') as file:
        file.write(f"Point: {point}\n")

        file.write(f"Sequence: {sequence}\n")

        file.write(f"{coordinate}")

    print(f"File berhasil disimpan di {file_path}")

def write_file2(result, point, matrix):
    folder_path = os.path.join(os.path.abspath('.'), 'test')
    file_name = input("Masukkan nama file (.txt): ")
    file_path = os.path.join(folder_path, f'{file_name}')

    if os.path.exists(file_path):
        overwrite = input("File dengan nama tersebut sudah ada. Apakah Anda ingin melakukan overwrite? (y/n): ").lower()
        if overwrite != 'y':
            while os.path.exists(file_path):
                file_name = input("Masukkan nama file (.txt): ")
                file_path = os.path.join(folder_path, f'{file_name}')
    
    sequence = sequence_string(result)
    coordinate = coordinate_string(result)

    with open(file_path, 'w') as file:
        file.write("Matriks:\n")
        for row in matrix:
            file.write(' '.join(map(str, row)) + '\n')

        file.write(f"Point: {point}\n")

        file.write(f"Sequence: {sequence}\n")

        file.write(f"{coordinate}")
    
    print(f"File berhasil disimpan di {file_path}")