class Solution:
    def removeDuplicates(self, s: str) -> str:
        if not s:
            return s

        container = []
        for char in s:
            if container and char == container[-1]:
                    container.pop()
            else:
                container.append(char)

        return ''.join(container)

s = Solution()
print(s.removeDuplicates("abbaca"))
