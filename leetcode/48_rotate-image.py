def rotate(matrix) -> None:
    n_row = len(matrix)
    if n_row < 2:
        return
    n_col = len(matrix[0])

    for i in range(n_row//2):
        for j in range(i, n_col-i-1):
            tmp = [matrix[i][j]]
            for _ in range(4):
                i, j = j, n_col - i - 1
                tmp.append(matrix[i][j])
                matrix[i][j] = tmp[0]
                tmp.pop(0)

matrix = [
    [ 5, 1, 9,11],
    [ 2, 4, 8,10],
    [13, 3, 6, 7],
    [15,14,12,16]
]

rotate(matrix)

print(matrix)