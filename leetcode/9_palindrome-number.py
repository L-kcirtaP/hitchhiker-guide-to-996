class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        if x == 0: return True

        n_digits = 10
        while (x / 10 ** (n_digits - 1) < 1): 
            n_digits -= 1

        lst = []
        for i in reversed(range(n_digits)):
            lst.append((int) (x / 10 ** i))
            x -= (int) (x / 10 ** i) * 10 ** i

        leng = len(lst)
        half_leng = (int) (leng / 2);
        for i in range(half_leng):
            if (lst[i] != lst[leng - i - 1]): return False
            
        return True
