class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if (needle == ""):
            return 0
        size_1, size_2 = len(haystack), len(needle)
        needle_first = needle[0]
        needle_last = needle[size_2 - 1]
        for pos in range(size_1):
            if haystack[pos] == needle_first and pos + size_2 - 1 < size_1 and haystack[pos + size_2 - 1] == needle_last:
                i, j = pos + 1, 1
                while i < size_1 and j  < size_2:
                    if haystack[i] != needle[j]:
                        break
                    i += 1; j += 1;
                if j == size_2:
                    return pos
        return -1
