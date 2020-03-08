def longestCommonPrefix(strs) -> str:
	if not strs:
		return ''

	prefix = ''
	zipped = list(zip(*strs))
	for i in range(len(zipped)):
		if all(char == zipped[i][0] for char in zipped[i]):
			prefix += zipped[i][0]
		else:
			break

	return prefix

print(longestCommonPrefix(["flower","flow","flight"]))
