class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        #either choose or don't choose
        nums.sort()
        res = [[]]
        prev_start = 0

        for i in range(len(nums)):
            #If the current number is the same as the previous one,
            # only attach it to the subsets added during the previous turn.
            start = prev_start if (i > 0 and nums[i] == nums[i-1]) else 0
            prev_start = len(res)

            for j in range(start, prev_start):
                res.append(res[j] + [nums[i]])

        return res
            