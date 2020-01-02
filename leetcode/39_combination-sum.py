class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        soln_set = []
        self.dfs(candidates, target, 0, [], soln_set)
        return soln_set

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
            self.dfs(candidates, target - cur, i, path+[cur], soln_set)
