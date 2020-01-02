class Solution:
    def maxArea(self, height: List[int]) -> int:
        start, end = 0, len(height) - 1
        maxV = 0
        while (start < end):
            if height[start] < height[end]:
                area = height[start] * (end - start)
                start += 1
            else:
                area = height[end] * (end - start)
                end -= 1
            maxV = max(maxV, area)
            
        return maxV
