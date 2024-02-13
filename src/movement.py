from util import *

def horizontal_first(sequences, num_sequences, matrix_size, matrix, points, buffer_size):
    point = 0
    result = []

    for x in range(num_sequences):
        sequence = sequences[x]
        
        for i in range(1, matrix_size[0]):
            for j in range(matrix_size[1]):
                if matrix[i][j] == sequence[0]:
                    temp_result = []
                    current_seq_checked = x
                    temp_result.append((i, j, 1, matrix[i][j]))
                    num = 1
                    move = 1
                    temp_matrix = duplicate_matrix(matrix)
                    start_i = i
                    start_j = j
                    length = len(sequence)
                    found_sequence = []
                    indicator = 0

                    while temp_matrix[i][j] != None:
                        isFound = True
                        while len(temp_result) < length and isFound and num <= len(sequences[current_seq_checked]) - 1:
                            move = temp_result[-1][2]
                    
                            if move == 1:
                                isFound = False
                                hor = 0
                                while hor < matrix_size[1] and not isFound:
                                    if temp_matrix[start_i][hor] == sequence[num] and hor != start_j:
                                        isFound = True
                                        if (start_i, hor, 0, temp_matrix[start_i][hor]) not in temp_result:
                                            temp_result.append((start_i, hor, 0, temp_matrix[start_i][hor]))
                                        num += 1
                                        start_j = hor
                                    hor += 1
                                    
                            elif move == 0:
                                isFound = False
                                ver = 0
                                while ver < matrix_size[0] and not isFound:
                                    if temp_matrix[ver][start_j] == sequence[num] and ver != start_i:
                                        isFound = True
                                        if (ver, start_j, 1, temp_matrix[ver][start_j]) not in temp_result:
                                            temp_result.append((ver, start_j, 1, temp_matrix[ver][start_j]))
                                        num += 1
                                        start_i = ver
                                    ver += 1
                        
                        if len(temp_result) == length:
                            if temp_result == result:
                                temp_matrix[temp_result[-1][0]][temp_result[-1][1]] = None
                                temp_result = [(i, j, 1, matrix[i][j])]
                                num = 1
                                start_i = i
                                start_j = j
                            else:
                                if current_seq_checked not in found_sequence:
                                    found_sequence.append(current_seq_checked)
                                temp_point = check_sequence(temp_result, sequences, num_sequences, points)
                                if temp_point > point:
                                    point = temp_point
                                    result = temp_result.copy()

                                if len(found_sequence) == num_sequences:
                                    return result, point
                                else:
                                    base = temp_result.copy()
                                    for y in range(num_sequences):
                                        if y not in found_sequence and temp_result[-1][3] == sequences[y][0]:
                                            if temp_result[-1][2] == 1:
                                                if check_horizontal(sequences[y][1], temp_matrix, matrix_size, temp_result[-1][0]) and length+len(sequences[y]) <= buffer_size:
                                                    current_seq_checked = y
                                                    length += len(sequences[y])-1
                                                    sequence = sequences[y]
                                                    num = 1
                                                    indicator = 1
                                                elif check_horizontal(sequences[y][1], temp_matrix, matrix_size, temp_result[-1][0]) and length+len(sequences[y]) > buffer_size:
                                                    temp_matrix[temp_result[-1][0]][temp_result[-1][1]] = None
                                                    temp_result = [(i, j, 1, matrix[i][j])]
                                                    num = 1
                                                    start_i = i
                                                    start_j = j
                                            
                                            elif temp_result[-1][2] == 0:
                                                if check_vertical(sequences[y][1], temp_matrix, matrix_size, temp_result[-1][1]) and length+len(sequences[y]) <= buffer_size:
                                                    current_seq_checked = y
                                                    length += len(sequences[y])-1
                                                    sequence = sequences[y]
                                                    num = 1
                                                    indicator = 1
                                                elif check_vertical(sequences[y][1], temp_matrix, matrix_size, temp_result[-1][1]) and length+len(sequences[y]) > buffer_size:
                                                    temp_matrix[temp_result[-1][0]][temp_result[-1][1]] = None
                                                    temp_result = [(i, j, 1, matrix[i][j])]
                                                    num = 1
                                                    start_i = i
                                                    start_j = j
                                            

                                        elif y not in found_sequence and temp_result[-1][3] != sequences[y][0]:
                                            if temp_result[-1][2] == 1:
                                                if check_horizontal(sequences[y][0], temp_matrix, matrix_size, temp_result[-1][0]) and length+len(sequences[y]) <= buffer_size-1:
                                                    current_seq_checked = y
                                                    length += len(sequences[y])
                                                    sequence = sequences[y]
                                                    num = 0
                                                    indicator = -1
                                                elif check_horizontal(sequences[y][0], temp_matrix, matrix_size, temp_result[-1][0]) and length+len(sequences[y]) > buffer_size-1:
                                                    temp_matrix[temp_result[-1][0]][temp_result[-1][1]] = None
                                                    temp_result = [(i, j, 1, matrix[i][j])]
                                                    num = 1
                                                    start_i = i
                                                    start_j = j
                                                else:
                                                    temp_matrix[temp_result[-1][0]][temp_result[-1][1]] = None
                                                    temp_result = [(i, j, 1, matrix[i][j])]
                                                    num = 1
                                                    start_i = i
                                                    start_j = j

                                            elif temp_result[-1][2] == 0:
                                                if check_vertical(sequences[y][0], temp_matrix, matrix_size, temp_result[-1][1]) and length+len(sequences[y]) <= buffer_size-1:
                                                    current_seq_checked = y
                                                    length += len(sequences[y])
                                                    sequence = sequences[y]
                                                    num = 0
                                                    indicator = -1
                                                elif check_vertical(sequences[y][0], temp_matrix, matrix_size, temp_result[-1][1]) and length+len(sequences[y]) > buffer_size-1:
                                                    temp_matrix[temp_result[-1][0]][temp_result[-1][1]] = None
                                                    temp_result = [(i, j, 1, matrix[i][j])]
                                                    num = 1
                                                    start_i = i
                                                    start_j = j
                                                else:
                                                    temp_matrix[temp_result[-1][0]][temp_result[-1][1]] = None
                                                    temp_result = [(i, j, 1, matrix[i][j])]
                                                    num = 1
                                                    start_i = i
                                                    start_j = j

                                            

                        else:
                            temp_matrix[temp_result[-1][0]][temp_result[-1][1]] = None
                            
                            if indicator == 1:
                                if check_horizontal(sequences[current_seq_checked][1], temp_matrix, matrix_size, temp_result[-1][0]):
                                    temp_result = base
                                    start_i = temp_result[-1][0]
                                    start_j = temp_result[-1][1]
                                    num = 1
                                else:
                                    temp_result = [(i, j, 1, matrix[i][j])]
                                    num = 1
                                    start_i = i
                                    start_j = j
                            elif indicator == -1:
                                if check_vertical(sequences[current_seq_checked][1], temp_matrix, matrix_size, temp_result[-1][1]):
                                    temp_result = base
                                    start_i = temp_result[-1][0]
                                    start_j = temp_result[-1][1]
                                    num = 1
                                else:
                                    temp_result = [(i, j, 1, matrix[i][j])]
                                    num = 1
                                    start_i = i
                                    start_j = j
                            else:
                                temp_result = [(i, j, 1, matrix[i][j])]
                                num = 1
                                start_i = i
                                start_j = j

    return result, point

def vertical_first(sequences, num_sequences, matrix_size, matrix, points, buffer_size):
    point = 0
    result = []

    for x in range(num_sequences):
        sequence = sequences[x]

    for x in range(num_sequences):
        sequence = sequences[x]
        result = []

        for i in range(matrix_size[0]):
            for j in range(matrix_size[1]):
                if matrix[i][j] == sequence[0]:
                    temp_result = []
                    current_seq_checked = x
                    temp_result.append((i, j, 1, matrix[i][j]))
                    num = 1
                    move = 1
                    temp_matrix = duplicate_matrix(matrix)
                    start_i = i
                    start_j = j
                    length = len(sequence)
                    found_sequence = []
                    indicator = 0

                    while temp_matrix[i][j] != None:
                        isFound = True
                        while len(temp_result) < length and isFound and num <= len(sequences[current_seq_checked]) - 1:
                            move = temp_result[-1][2]
                    
                            if move == 1:
                                isFound = False
                                hor = 0
                                while hor < matrix_size[1] and not isFound:
                                    if temp_matrix[start_i][hor] == sequence[num] and hor != start_j:
                                        isFound = True
                                        if (start_i, hor, 0, temp_matrix[start_i][hor]) not in temp_result:
                                            temp_result.append((start_i, hor, 0, temp_matrix[start_i][hor]))
                                        num += 1
                                        start_j = hor
                                    hor += 1
                                    
                            elif move == 0:
                                isFound = False
                                ver = 0
                                while ver < matrix_size[0] and not isFound:
                                    if temp_matrix[ver][start_j] == sequence[num] and ver != start_i:
                                        isFound = True
                                        if (ver, start_j, 1, temp_matrix[ver][start_j]) not in temp_result:
                                            temp_result.append((ver, start_j, 1, temp_matrix[ver][start_j]))
                                        num += 1
                                        start_i = ver
                                    ver += 1

                        if len(temp_result) == length:
                            if temp_result == result:
                                temp_matrix[temp_result[-1][0]][temp_result[-1][1]] = None
                                temp_result = [(i, j, 1, matrix[i][j])]
                                num = 1
                                start_i = i
                                start_j = j
                            else:
                                if current_seq_checked not in found_sequence:
                                    found_sequence.append(current_seq_checked)
                                temp_point = check_sequence(temp_result, sequences, num_sequences, points)
                                if temp_point > point:
                                    point = temp_point
                                    result = temp_result.copy()
                        
                            if len(found_sequence) == num_sequences:
                                return result, point
                            else:
                                base = temp_result.copy()
                                for y in range(num_sequences):
                                        if y not in found_sequence and temp_result[-1][3] == sequences[y][0]:
                                            if temp_result[-1][2] == 1:
                                                if check_horizontal(sequences[y][1], temp_matrix, matrix_size, temp_result[-1][0]) and length+len(sequences[y]) <= buffer_size:
                                                    current_seq_checked = y
                                                    length += len(sequences[y])-1
                                                    sequence = sequences[y]
                                                    num = 1
                                                    indicator = 1
                                                elif check_horizontal(sequences[y][1], temp_matrix, matrix_size, temp_result[-1][0]) and length+len(sequences[y]) > buffer_size:
                                                    temp_matrix[temp_result[-1][0]][temp_result[-1][1]] = None
                                                    temp_result = [(i, j, 1, matrix[i][j])]
                                                    num = 1
                                                    start_i = i
                                                    start_j = j
                                            
                                            elif temp_result[-1][2] == 0:
                                                if check_vertical(sequences[y][1], temp_matrix, matrix_size, temp_result[-1][1]) and length+len(sequences[y]) <= buffer_size:
                                                    current_seq_checked = y
                                                    length += len(sequences[y])-1
                                                    sequence = sequences[y]
                                                    num = 1
                                                    indicator = 1
                                                elif check_vertical(sequences[y][1], temp_matrix, matrix_size, temp_result[-1][1]) and length+len(sequences[y]) > buffer_size:
                                                    temp_matrix[temp_result[-1][0]][temp_result[-1][1]] = None
                                                    temp_result = [(i, j, 1, matrix[i][j])]
                                                    num = 1
                                                    start_i = i
                                                    start_j = j
                                            

                                        elif y not in found_sequence and temp_result[-1][3] != sequences[y][0]:
                                            if temp_result[-1][2] == 1:
                                                if check_horizontal(sequences[y][0], temp_matrix, matrix_size, temp_result[-1][0]) and length+len(sequences[y]) <= buffer_size-1:
                                                    current_seq_checked = y
                                                    length += len(sequences[y])
                                                    sequence = sequences[y]
                                                    num = 0
                                                    indicator = -1
                                                elif check_horizontal(sequences[y][0], temp_matrix, matrix_size, temp_result[-1][0]) and length+len(sequences[y]) > buffer_size-1:
                                                    temp_matrix[temp_result[-1][0]][temp_result[-1][1]] = None
                                                    temp_result = [(i, j, 1, matrix[i][j])]
                                                    num = 1
                                                    start_i = i
                                                    start_j = j
                                                else:
                                                    temp_matrix[temp_result[-1][0]][temp_result[-1][1]] = None
                                                    temp_result = [(i, j, 1, matrix[i][j])]
                                                    num = 1
                                                    start_i = i
                                                    start_j = j

                                            elif temp_result[-1][2] == 0:
                                                if check_vertical(sequences[y][0], temp_matrix, matrix_size, temp_result[-1][1]) and length+len(sequences[y]) <= buffer_size-1:
                                                    current_seq_checked = y
                                                    length += len(sequences[y])
                                                    sequence = sequences[y]
                                                    num = 0
                                                    indicator = -1
                                                elif check_vertical(sequences[y][0], temp_matrix, matrix_size, temp_result[-1][1]) and length+len(sequences[y]) > buffer_size-1:
                                                    temp_matrix[temp_result[-1][0]][temp_result[-1][1]] = None
                                                    temp_result = [(i, j, 1, matrix[i][j])]
                                                    num = 1
                                                    start_i = i
                                                    start_j = j
                                                else:
                                                    temp_matrix[temp_result[-1][0]][temp_result[-1][1]] = None
                                                    temp_result = [(i, j, 1, matrix[i][j])]
                                                    num = 1
                                                    start_i = i
                                                    start_j = j

                                            

                        else:
                            temp_matrix[temp_result[-1][0]][temp_result[-1][1]] = None
                            
                            if indicator == 1:
                                if check_horizontal(sequences[current_seq_checked][1], temp_matrix, matrix_size, temp_result[-1][0]):
                                    temp_result = base
                                    start_i = temp_result[-1][0]
                                    start_j = temp_result[-1][1]
                                    num = 1
                                else:
                                    temp_result = [(i, j, 1, matrix[i][j])]
                                    num = 1
                                    start_i = i
                                    start_j = j
                            elif indicator == -1:
                                if check_vertical(sequences[current_seq_checked][1], temp_matrix, matrix_size, temp_result[-1][1]):
                                    temp_result = base
                                    start_i = temp_result[-1][0]
                                    start_j = temp_result[-1][1]
                                    num = 1
                                else:
                                    temp_result = [(i, j, 1, matrix[i][j])]
                                    num = 1
                                    start_i = i
                                    start_j = j
                            else:
                                temp_result = [(i, j, 1, matrix[i][j])]
                                num = 1
                                start_i = i
                                start_j = j
                        
    return result, point