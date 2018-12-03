def main(input_file, matrix_n):
    matrix = create_matrix(matrix_n)
    matrix_filled = fill_matrix(matrix, input_file)
    find_no_overlap(matrix_filled, input_file)
    index_matrix = find_x(matrix_filled)

    squares = 0
    for x in index_matrix:
        squares += len(x)
    print(squares)


def create_matrix(n):
    return [[0 for x in range(n)] for y in range(n)]


def fill_matrix(matrix, input_file):
    with open(input_file) as f:
        for line in f:
            line = line.strip()
            line_parts = line.split()
            start = line_parts[2][:-1].split(",")
            size = line_parts[3].split("x")
            for i in range(int(size[0])):
                for j in range(int(size[1])):
                    col = int(start[0]) + i
                    row = int(start[1]) + j
                    matrix[col][row] += 1

    f.close()
    return matrix


def find_no_overlap(matrix, input_file):
    with open(input_file) as f:
        for line in f:
            line = line.strip()
            line_parts = line.split()
            FLAG = 1
            claim_id = line_parts[0]
            start = line_parts[2][:-1].split(",")
            size = line_parts[3].split("x")
            for i in range(int(size[0])):
                for j in range(int(size[1])):
                    col = int(start[0]) + i
                    row = int(start[1]) + j
                    if matrix[col][row] > 1:
                        FLAG = 0

            if FLAG == 1:
                no_overlap_id = claim_id

        print("ID with no overlap: " + str(no_overlap_id))


def find_x(matrix):
    index_matrix = []

    for x in matrix:
        indexes = [i for i, n in enumerate(x) if n >= 2]
        if indexes:
            index_matrix.append(indexes)

    return index_matrix


if __name__ == '__main__':
    input_f = "input_1.txt"
    main(input_f, matrix_n=1000)
