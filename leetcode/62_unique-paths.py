def uniquePaths(m: int, n: int) -> int:
    import math
    f = math.factorial
    return int(f(m+n-2) / f(m-1) / f(n-1))

print(uniquePaths(3, 7))