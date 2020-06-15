#### Question 1
import sys

n = int(sys.stdin.readline().strip())
balls = list(map(int, sys.stdin.readline().strip().split(' ')))

def solution(n, balls):
	res = 0
	occr = {}
	for i in balls:
		occr[i] = occr.get(i, 0) + 1

	for i in balls:
		if occr[i] > 1:
			# handle it
			foo = i
			# print(foo)
			while occr[i] != 1:
				if foo not in occr:
					res += foo - i
					occr[foo] = 1
					occr[i] -= 1
				foo += 1

	return res

res = solution(4, [1, 3, 1, 4])
print(res)


#### Question 2
import sys

T = int(sys.stdin.readline().strip())
comb = []
for _ in range(T):
	comb.append(list(map(int, sys.stdin.readline().strip().split(' '))))


def test_cube(sticks):
	if sum(sticks) % 4:
		return False

	length = sum(sticks)/4

	sticks.sort(reverse=True)
	start, end = 0, len(sticks)-1
	if sticks[start] > length: return False
	if sticks[end] == length: return True

	while start < end:
		if sticks[start] == length:
			start += 1
		else:
			cur = sticks[start] + sticks[end]
			if cur > length: return False
			while cur < length:
				end -= 1
				cur += sticks[end]
				if cur > length: return False
				if start >= end: return False
			start += 1
			end -= 1

	return True

for sticks in comb:
	print('YES' if test_cube(sticks[1:]) else 'NO')


#### Question 3
import sys

T = int(sys.stdin.readline().strip())
combs = []
for _ in range(T):
	combs.append(list(map(int, sys.stdin.readline().strip().split(' '))))


def fibonacci(A, B, n):
	arr = [A, B]
	for _ in range(n-1):
		tar = sum(arr)
		arr[0], arr[1] = arr[1], tar

	return True if arr[1] % 3 == 0 else False

for comb in combs:
	print('YES' if fibonacci(comb[0], comb[1], comb[2]) else 'NO')


#### Question 4

import sys

n = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().strip().split(' ')))

def gcd(a, b):
	if a % b == 0:
		return b
	return gcd(b, a % b)

gcds = [[1] * n for i in range(n)]

for i in range(n):
	gcds[i][i] = arr[i]

for j in range(1, n):
	for i in range(j):
		print(i,j)
		gcds[i][j] = gcd(gcds[i][j-1], arr[j])

for j in range(1, n):
	for i in range(j):
		gcds[i][j] = gcds[i][j] * (j-i+1)

print(max([max(i) for i in gcds]))
