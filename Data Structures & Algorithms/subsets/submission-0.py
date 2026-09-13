class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i: int):
            #base case: we've decided on all elements
            if i >= len(nums):
                res.append(subset.copy()) #must take a copy/snapshot
                return

            #choice 1: include nums[i]
            subset.append(nums[i])
            dfs(i+1)

            #backtrack: undo thte choice
            subset.pop()

            #choice 2: exclude nums[i]
            dfs(i+1)
        
        dfs(0)
        return res
        