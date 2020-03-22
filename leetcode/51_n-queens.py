def solveNQueens(n: int):
    if n == 0:
        return []

    result = []
    NQueensCore([0]*n, 0, result)
    return result

def NQueensCore(board, column, res):
    if column == len(board):
        solution = list(board)
        res.append(['.'*(queen)+'Q'+'.'*(len(board)-queen-1) for queen in solution])
        return

    for i in range(len(board)):        
        board[column] = i
        if is_valid(board, column):
            NQueensCore(board, column+1, res)


def is_valid(board, column):
    valid = True
    for i in range(column):
        valid &= not (board[column] == board[i] or abs(board[column]-board[i]) == column-i)
        if not valid:
            return valid
    return valid
