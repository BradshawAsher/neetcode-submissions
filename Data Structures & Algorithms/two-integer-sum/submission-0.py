class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #1 pass
        #for every value, add the target-num to a dict
        #dict will be k=value, v=index of first
        #when we go through the list, if we find a dict match, then return i and j
        #else return []

        diffs = {}

        for i in range(len(nums)):
            num = nums[i]
            if num in diffs:
                return [diffs[num], i]
            else:
                gap = target-num
                #check if gap in dict
                if gap not in diffs:
                    #add to diffs
                    diffs[gap] = i
        return []