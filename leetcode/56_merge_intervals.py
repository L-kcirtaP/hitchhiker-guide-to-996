def merge(intervals):
	if not intervals:
		return []

	intervals.sort()
	foo = []
	for i in range(len(intervals)):
		interval = intervals[i]
		if i == 0 or interval[0] > foo[-1]:
			foo += interval

		elif interval[1] > foo[-1]:
			foo.pop()
			foo.append(interval[1])

	return [(foo[i], foo[i+1]) for i in range(0, len(foo), 2)]

intervals = [[1,4],[4,5]]
print(merge(intervals))
