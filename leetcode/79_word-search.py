def exist(board, word) -> bool:
	if not word:
		return True
	if not board:
		return False

	height = len(board)
	width = len(board[0])
	visited = [[False for i in range(width)] for j in range(height)]
	for i in range(height):
		for j in range(width):
			if existAt(board, i, j, height, width, 0, word, visited):
				return True
	return False


def existAt(board, i, j, height, width, pos, word, visited):
	if pos == len(word):
		return True

	existed = False
	if i >= 0 and j >= 0 and i < height and j < width and not visited[i][j] and board[i][j] == word[pos]:
		visited[i][j] = True
		existed = existAt(board, i+1, j, height, width, pos+1, word, visited)\
				| existAt(board, i-1, j, height, width, pos+1, word, visited)\
				| existAt(board, i, j+1, height, width, pos+1, word, visited)\
				| existAt(board, i, j-1, height, width, pos+1, word, visited)
		if not existed:
			visited[i][j] = False

	return existed

board = [
	["C","A","A"],
	["A","A","A"],
	["B","C","D"]]
word = 'AAB'
ret = exist(board, word)
print(ret)
