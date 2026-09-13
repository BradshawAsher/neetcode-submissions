class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #essentially make as many combinations as possible can reuse, but terminate if the sum goes above target
        res = []
        subset = []

        def dfs(i: int, remaining: int):
            #base case 1: found valid combination
            if remaining == 0:
                res.append(subset.copy())
                return

            #base case 2: exceeded target or exhausted nums
            if remaining < 0 or i >= len(nums):
                return

            #choice 1: include nums[i] (stay at index i to allow reuse)
            subset.append(nums[i])
            dfs(i, remaining - nums[i])
            
            #backtrack
            subset.pop()

            #choice 2: exclude nums[i] (move to i+1)
            dfs(i+1, remaining)

        dfs(0, target)
        return res