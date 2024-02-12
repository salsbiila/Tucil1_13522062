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
                        # print("length: ", length)
                        # print("temo_matrix[i][j]: ", temp_matrix[i][j])
                        # print("temp_matrix: ")
                        # for row in temp_matrix:
                            # print(row)
                        isFound = True
                        while len(temp_result) < length and isFound and num <= len(sequences[current_seq_checked]) - 1:
                            # print("start_i: ", start_i)
                            # print("start_j: ", start_j)
                            move = temp_result[-1][2]
                            # print("move: ", move)
                    
                            if move == 1:
                                # print("kok")
                                isFound = False
                                hor = 0
                                while hor < matrix_size[1] and not isFound:
                                    # print("sequence[num] hor: ", sequence[num])
                                    # print("sequence[num]: ", sequence[num])
                                    if temp_matrix[start_i][hor] == sequence[num] and hor != start_j:
                                        isFound = True
                                        # print("isfound awal: ", isFound)
                                        if (start_i, hor, 0, temp_matrix[start_i][hor]) not in temp_result:
                                            temp_result.append((start_i, hor, 0, temp_matrix[start_i][hor]))
                                        # print("sequence[num]: ", sequence[num])
                                        num += 1
                                        start_j = hor
                                    hor += 1
                                # print("isfound: ", isFound)
                                # print("num: ", num)
                                # print("temp_result abis hor: ", temp_result)
                                    
                            elif move == 0:
                                # print("pip")
                                isFound = False
                                ver = 0
                                while ver < matrix_size[0] and not isFound:
                                    # print("sequence[num] ver: ", sequence[num])
                                    # print("temp_matrix[ver][start_j]: ", temp_matrix[ver][start_j])
                                    # print("start_i: ", start_i)
                                    if temp_matrix[ver][start_j] == sequence[num] and ver != start_i:
                                        isFound = True
                                        # print("isfound awal: ", isFound)
                                        if (ver, start_j, 1, temp_matrix[ver][start_j]) not in temp_result:
                                            temp_result.append((ver, start_j, 1, temp_matrix[ver][start_j]))
                                        # print("sequence[num]: ", sequence[num])
                                        num += 1
                                        start_i = ver
                                    ver += 1
                                # print("temp_result abis ver: ", temp_result)
                                # print("isfound: ", isFound)
                        
                        # print("temp_result: ", temp_result)
                        # print("-------------------")
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
                                # print("result: ", result)
                                # print("point: ", point)
                                # print("temp_point: ", temp_point)
                                # print("temp_result di akhir: ", temp_result)
                                if temp_point > point:
                                    point = temp_point
                                    result = temp_result.copy()

                                if len(found_sequence) == num_sequences:
                                    # print("found_sequence: ", found_sequence)
                                    # print("nume_sequence: ", num_sequences)
                                    return result, point
                                else:
                                    # print("temp_result sblm base: ", temp_result)
                                    base = temp_result.copy()
                                    # print("temp result setelah base: ", temp_result)
                                    for y in range(num_sequences):
                                        # print("temp_result di mari: ", temp_result)
                                        # print("y: ", y)
                                        if y not in found_sequence and temp_result[-1][3] == sequences[y][0]:
                                            # print("temp_result di sana: ", temp_result)
                                            # print("Masuk sini")
                                            if temp_result[-1][2] == 1:
                                                # print("weh")
                                                # print("sequences[y][1]: ", sequences[y][1])
                                                if check_horizontal(sequences[y][1], temp_matrix, matrix_size, temp_result[-1][0]) and length+len(sequences[y]) <= buffer_size:
                                                    current_seq_checked = y
                                                    length += len(sequences[y])-1
                                                    sequence = sequences[y]
                                                    num = 1
                                                    indicator = 1
                                                    # print("loh")
                                                    # print("temp_result di sini: ", temp_result)
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
                                            # print("bentar")
                                            if temp_result[-1][2] == 1:
                                                if check_horizontal(sequences[y][0], temp_matrix, matrix_size, temp_result[-1][0]) and length+len(sequences[y]) <= buffer_size-1:
                                                    current_seq_checked = y
                                                    length += len(sequences[y])
                                                    sequence = sequences[y]
                                                    # print("Sequence yg mau dicari: ", sequence)
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
                                                    # print("Sequence yg mau dicari: ", sequence)
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
                            # print("temp_matrix: ")
                            # for row in temp_matrix:
                            #     print(row)
                            
                            
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

                            # if (len(found_sequence) == 0) or (len(found_sequence) > 0 and not isFound):
                            #     temp_result = [(i, j, 1, matrix[i][j])]
                            #     num = 1
                            #     start_i = i
                            #     start_j = j
                                # print("duh")
                            # else:
                            #     temp_result = base
                            #     start_i = temp_result[-1][0]
                            #     start_j = temp_result[-1][1]
                            #     if indicator == 1:
                            #         num = 1
                            #     elif indicator == -1:
                            #         num = 0
                                # print("lol")

                        
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
                            # print("start_i: ", start_i)
                            # print("start_j: ", start_j)
                            move = temp_result[-1][2]
                            # print("move: ", move)
                    
                            if move == 1:
                                isFound = False
                                hor = 0
                                while hor < matrix_size[1] and not isFound:
                                    if temp_matrix[start_i][hor] == sequence[num] and hor != start_j:
                                        isFound = True
                                        # print("isfound awal: ", isFound)
                                        if (start_i, hor, 0, temp_matrix[start_i][hor]) not in temp_result:
                                            temp_result.append((start_i, hor, 0, temp_matrix[start_i][hor]))
                                        # print("sequence[num]: ", sequence[num])
                                        num += 1
                                        start_j = hor
                                    hor += 1
                                # print("isfound: ", isFound)
                                # print("num: ", num)
                                    
                            elif move == 0:
                                isFound = False
                                ver = 0
                                while ver < matrix_size[0] and not isFound:
                                    # print("temp_matrix[ver][start_j]: ", temp_matrix[ver][start_j])
                                    if temp_matrix[ver][start_j] == sequence[num] and ver != start_i:
                                        isFound = True
                                        # print("isfound awal: ", isFound)
                                        if (ver, start_j, 1, temp_matrix[ver][start_j]) not in temp_result:
                                            temp_result.append((ver, start_j, 1, temp_matrix[ver][start_j]))
                                        # print("sequence[num]: ", sequence[num])
                                        num += 1
                                        start_i = ver
                                    ver += 1
                                # print("isfound: ", isFound)
                        
                        # print("temp_result: ", temp_result)
                        # print("-------------------")
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
                                # print("result: ", result)
                                # print("point: ", point)
                                # print("temp_point: ", temp_point)
                                # print("temp_result di akhir: ", temp_result)
                                if temp_point > point:
                                    point = temp_point
                                    result = temp_result.copy()
                        
                            if len(found_sequence) == num_sequences:
                                # print("found_sequence: ", found_sequence)
                                # print("nume_sequence: ", num_sequences)
                                return result, point
                            else:
                                base = temp_result.copy()
                                for y in range(num_sequences):
                                        # print("temp_result di mari: ", temp_result)
                                        # print("y: ", y)
                                        if y not in found_sequence and temp_result[-1][3] == sequences[y][0]:
                                            # print("temp_result di sana: ", temp_result)
                                            # print("Masuk sini")
                                            if temp_result[-1][2] == 1:
                                                # print("weh")
                                                # print("sequences[y][1]: ", sequences[y][1])
                                                if check_horizontal(sequences[y][1], temp_matrix, matrix_size, temp_result[-1][0]) and length+len(sequences[y]) <= buffer_size:
                                                    current_seq_checked = y
                                                    length += len(sequences[y])-1
                                                    sequence = sequences[y]
                                                    num = 1
                                                    indicator = 1
                                                    # print("loh")
                                                    # print("temp_result di sini: ", temp_result)
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
                                            # print("bentar")
                                            if temp_result[-1][2] == 1:
                                                if check_horizontal(sequences[y][0], temp_matrix, matrix_size, temp_result[-1][0]) and length+len(sequences[y]) <= buffer_size-1:
                                                    current_seq_checked = y
                                                    length += len(sequences[y])
                                                    sequence = sequences[y]
                                                    print("Sequence yg mau dicari: ", sequence)
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
                                                    # print("Sequence yg mau dicari: ", sequence)
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
                            # print("temp_matrix: ")
                            # for row in temp_matrix:
                            #     print(row)
                            
                            
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