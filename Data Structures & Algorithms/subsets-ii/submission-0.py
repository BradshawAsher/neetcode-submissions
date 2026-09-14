class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        #either choose or don't choose
        nums.sort() #1. must sort to bring identical values together

        res = []
        subset = []

        def dfs(i: int):
            #Base case: we have decided include/exclude for all elements
            if i == len(nums):
                res.append(subset.copy())
                return

            #case 1: include nums[i]
            subset.append(nums[i])
            dfs(i+1)
            subset.pop()

            #case 2: exclude nums[i]
            #skip all adjacent duplicates so we don't branch into an identical subproblem
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            dfs(i+1)

        dfs(0)
        return res

            