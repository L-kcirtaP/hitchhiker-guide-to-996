class Solution:
    def reverse(self, x: int) -> int:
        if x == 0: return x
        
        n_digits = 10
        neg = False if x > 0 else True
        x = abs(x)

        while (x / 10 ** (n_digits - 1) < 1): 
            n_digits -= 1
        ret = 0

        for i in reversed(range(n_digits)):
            ret += (int) (x / 10 ** i) * 10 ** (n_digits - i - 1)
            x -= (int) (x / 10 ** i) * 10 ** i

        if ret > 2**31 -1: return 0

        return ret if neg == False else -ret
