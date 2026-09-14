class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        candidates.sort()

        def dfs(start: int, remaining: int):

            #base case
            if remaining == 0:
                res.append(subset.copy())
                return

            for i in range(start, len(candidates)):
                #Prune: subsequent numbers will also be too large since candidates is sorted
                if candidates[i] > remaining:
                    break

                #skip duplicate elements at the same recursion depth
                if i > start and candidates[i] == candidates[i-1]:
                    continue

                subset.append(candidates[i])
                dfs(i+1, remaining - candidates[i])
                subset.pop()
        dfs(0, target)
        return res
