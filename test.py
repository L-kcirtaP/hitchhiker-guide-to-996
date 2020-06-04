# import sys

# n = int(sys.stdin.readline().strip())
# data = []
# for _ in range(n):
# 	data.append(list(map(int, sys.stdin.readline().strip().split(' '))))

# results = [[0] * n for _ in range(n)]
# results[0][0] = data[0][0]

# for row in range(1, n):
# 	results[row][0] = data[row][0] + results[row-1][0]
# 	results[row][row] = data[row][row] + results[row-1][row-1]

# for row in range(n):
# 	for col in range(1, row):
# 		results[row][col] = data[row][col] + max(results[row-1][col-1], results[row-1][col])

# print(max(results[n-1]))


# n, k = map(int, sys.stdin.readline().strip().split(' '))
# arr = list(map(int, sys.stdin.readline().strip().split(' ')))

# arr.sort()

# start = k//2
# subarr = arr[start:start+k]
# avg = sum(subarr) // k

# print(min(sum([abs(i-avg) for i in subarr]), sum([abs(i-avg-1) for i in subarr])))


# n = int(sys.stdin.readline().strip())
# row = list(map(int, sys.stdin.readline().strip().split(' ')))

# result = 0
# for i in range(0, len(row), 2):
#     peer = row[i] ^ 1
#     if row[i+1] != peer:
#         j = i + 2 + row[i+2:].index(peer)
#         row[i+1], row[j], result = row[j], row[i+1], result+1 

# print(result)

# def count():
# 	fs = []
# 	for i in range(1,4):
# 		def f():
# 			return i * i
# 		fs.append(f)
# 	return fs

# import sys

# N = int(sys.stdin.readline().strip())
# nums = list(map(int, sys.stdin.readline().strip().split(' ')))

# def solveFrog(N, nums):
# 	dp = [0] * N
# 	dp[0] = 0
# 	for i in range(1, N):
# 		jump_1 = dp[i-1] + 1
# 		jump_2 = jump_1
# 		for j in range(i-1, -1, -1):
# 			if nums[i] == nums[j]:
# 				jump_2 = dp[j] + 1
# 				break
# 		dp[i] = min(jump_1, jump_2)

# 	return dp[N-1]

# import sys
# k = int(sys.stdin.readline().strip())

# groups = []
# for _ in range(k):
# 	n_rows = int(sys.stdin.readline().strip())
# 	board = []
# 	for i in range(n_rows):
# 		board.append(list(map(int, sys.stdin.readline().strip().split(' '))))
# 	groups.append(board)


# def validForEntry(board, row, col):
# 	up = down = left = right = 0
# 	if row > 0:
# 		up = int(board[row-1, col] == 'x')
# 	if row < len(board)-1:
# 		down = int(board[row+1, col] == 'x')
# 	if col > 0:
# 		left = int(board[row, col-1] == 'x')
# 	if col < len(board[0]) - 1:
# 		right = int(board[row, col+1] == 'x')
	
# 	return int(board[row][col]) == up + down + left + right


# def solveBoard(board):
# 	if not board:
# 		return []
# 	def core(board, row, res):
# 		n_unknown = len([i for i in range(board) if board[row][i] == '?'])	# 该行未知格子的数量

# 		for i in range(2**n_unknown):
# 			current_board = ?		# a placement of 'x' and 'o' on the board
# 			flag = True
# 			for col in board[row]:
# 				flag &= validForEntry(board, row, col)

# 			if flag:
# 				if row == len(board) - 1:
# 					res += 1
# 				else:
# 					core(board, row+1, res)

# 	res = 0
# 	core(board, 0, res)

# 	return res


# print([solveBoard(board) for board in groups])



# def lottery(n):
# 	import random
# 	with open('candidates.txt', 'r') as f:
# 		candidates = f.readlines()
# 	return random.sample(candidates, n)

# winners = lottery(34)

# print('======== 三等奖 * 30 ========')
# for i in range(30):
# 	print(winners[i])
# print('======== 二等奖 * 3 ========')
# for i in range(30, 33):
# 	print(winners[i])
# print('======== 一等奖 * 1 ========')
# for i in range(33, 34):
# 	print(winners[i])


# import random
# print(random.sample(range(13), 6))