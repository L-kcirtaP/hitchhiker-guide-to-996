### old solution: time limit exceeds
# def wordBreak(s: str, wordDict) -> bool:
# 	if not s:
# 		return True

# 	for pos in range(1, len(s)+1):
# 		cur = s[:pos]
# 		if cur in wordDict:
# 			if wordBreak(s[pos:], wordDict):
# 				return True
# 	return False

### better solution using dp
def wordBreak(s: str, wordDict) -> bool:
	dp = [True if i == 0 else False for i in range(len(s)+1)]

	for pos in range(1, len(s)+1):
		for prev in range(0, pos):
			if dp[prev] == True:
				if s[prev:pos] in wordDict:
					dp[pos] = True
	return dp[-1]

# print(wordBreak("applepenapple", ["apple", "pen"]))
print(wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
