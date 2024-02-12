import random

def generate_matrix(tokens, n, m):
    matrix = []
    for i in range(n):
        row = [random.choice(tokens) for i in range(m)]
        matrix.append(row)
    return matrix

def generate_sequences(tokens, num_sequences, max_sequence_length):
    sequences = []
    for i in range(num_sequences):
        sequence_length = random.randint(2, max_sequence_length)
        sequence = [random.choice(tokens) for i in range(sequence_length)]
        sequences.append(sequence)
    return sequences

def point_generator(num_sequences):
    points = []
    for i in range(num_sequences):
        points.append((random.randint(1, 20))*5)
    return points

def duplicate_matrix(matrix):
    return [row.copy() for row in matrix]

def check_horizontal(token, matrix, matrix_size, start_i):
    for j in range(matrix_size[1]):
        if matrix[start_i][j] == token:
            return True

def check_vertical(token, matrix, matrix_size, start_j):
    for i in range(matrix_size[0]):
        if matrix[i][start_j] == token:
            return True

def check_sequence(temp_result, sequences, num_sequences, points):
    string = ""
    point = 0

    for i in range(len(temp_result)):
        string += temp_result[i][3]
    
    for i in range(num_sequences):
        checker = ""
        for j in range(len(sequences[i])):
            checker += sequences[i][j]
        if checker in string:
            point += int(points[i])
    
    return point

def print_result(result, point):
    print("Point:", point)
    print("Sequence: ", end="")
    for i in range(len(result)):
        if i != len(result) - 1:
            print(result[i][3], end=" ")
        else:
            print(result[i][3])
    
    for i in range(len(result)):
        print(f"{result[i][0]},{result[i][1]}")

def sequence_string(result):
    string = ""
    for i in range(len(result)):
        if i != len(result) - 1:
            string += f"{result[i][3]} "
        else:
            string += f"{result[i][3]}"
    return string

def coordinate_string(result):
    string = ""
    for i in range(len(result)):
        if i != len(result) - 1:
            string += f"{result[i][0]},{result[i][1]}\n"
        else:
            string += f"{result[i][0]},{result[i][1]}"
    return string