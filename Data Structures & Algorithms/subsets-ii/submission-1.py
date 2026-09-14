class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        #either choose or don't choose
        nums.sort()

        res = []
        subset = []

        def dfs(start: int):
            res.append(subset.copy())

            for i in range(start, len(nums)):
                #skip duplicate elements at the current tree depth
                if i > start and nums[i] == nums[i-1]:
                    continue

                subset.append(nums[i])
                dfs(i+1)
                subset.pop()

        dfs(0)
        return res

            