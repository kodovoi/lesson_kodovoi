def get_matrix(n, m, value):
    matrix = []

    for i in range(n):
        row = []

        for j in range(m):
            row.append(value)
        matrix.append(row)

    return matrix

result_1 = get_matrix(2, 2, 10)
result_2 = get_matrix(3, 5, 42)
result_3 = get_matrix(4, 2, 13)
for row in result_1, result_2, result_3:
    print(row)
