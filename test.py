import sys

n = int(sys.stdin.readline().strip())
data = []
for _ in range(n):
	data.append(list(map(int, sys.stdin.readline().strip().split(' '))))

results = [[0] * n for _ in range(n)]
results[0][0] = data[0][0]

for row in range(1, n):
	results[row][0] = data[row][0] + results[row-1][0]
	results[row][row] = data[row][row] + results[row-1][row-1]

for row in range(n):
	for col in range(1, row):
		results[row][col] = data[row][col] + max(results[row-1][col-1], results[row-1][col])

print(max(results[n-1]))


n, k = map(int, sys.stdin.readline().strip().split(' '))
arr = list(map(int, sys.stdin.readline().strip().split(' ')))

arr.sort()

start = k//2
subarr = arr[start:start+k]
avg = sum(subarr) // k

print(min(sum([abs(i-avg) for i in subarr]), sum([abs(i-avg-1) for i in subarr])))


n = int(sys.stdin.readline().strip())
row = list(map(int, sys.stdin.readline().strip().split(' ')))

result = 0
for i in range(0, len(row), 2):
    peer = row[i] ^ 1
    if row[i+1] != peer:
        j = i + 2 + row[i+2:].index(peer)
        row[i+1], row[j], result = row[j], row[i+1], result+1 

print(result)


