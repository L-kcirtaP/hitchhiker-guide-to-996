class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
    	start, end, max_len = 0, 0, 0
    	while (end < len(s)):
    		end += 1
    		while not (len(set(s[start:end])) == len(s[start:end])):
    			start += 1
    		if (end - start) > max_len:
	    		max_len = end - start

    	return max_len
