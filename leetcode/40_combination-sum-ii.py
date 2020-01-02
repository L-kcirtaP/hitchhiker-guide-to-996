import itertools

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        soln_set = []
        candidates = sorted(candidates)
        self.dfs(candidates, target, 0, [], soln_set)
        soln_set.sort()
        return list(soln_set for soln_set, _ in itertools.groupby(soln_set))

    def dfs(self, candidates: List[int], target: int, start: int, path: List[int], soln_set: List[int]):
        if target < 0:
            return
        if target == 0:
            soln_set.append(path)
            return
        length = len(candidates)
        for i in range(start, length):
            cur = candidates[i]
            if cur > target:
                continue
            self.dfs(candidates, target - cur, i+1, path+[cur], soln_set)
