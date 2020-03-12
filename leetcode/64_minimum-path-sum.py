def minPathSum(grid) -> int:
	if not grid:
		return 0

	m = len(grid)
	n = len(grid[0])
	dp = [[0 for i in range(n)] for j in range(m)]

	for i in range(n):
		dp[0][i] = dp[0][i-1] + grid[0][i]
	for j in range(1, m):
		dp[j][0] = dp[j-1][0] + grid[j][0]

	for i in range(1, m):
		for j in range(1, n):
			dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

	return dp[m-1][n-1]


grid = [[1,2,5],[3,2,1]]
print(minPathSum(grid))
