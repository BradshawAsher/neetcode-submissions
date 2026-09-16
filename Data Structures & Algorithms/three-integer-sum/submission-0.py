class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #o(n^2) time and o(1) space

        #Understand
        #input = list of ints (non-sorted)
        #output = list of lists of group 3 where 3 distinct values at those indeces add up to 0

        #m - match = two pointers

        #Plan
        #well we need to choose 3 or 2 pointers and then like adjust pointers based on the sum
        #since it's o(n^2) we can choose like an anchor/pivot and then have 2 pointers around it???
        #technically we can have the anchor start at the beginning and go till len(nums)-2, where left = anchor + 1 and right = len(nums)-1 and like that
        nums.sort()

        res = []
        n = len(nums)

        for i in range(n-2):
            #optimization: if the smallest number is > 0, three pointers can never sum to 0
            if nums[i] > 0:
                break
            
            #skip duplicate anchors to avoid identical triplets
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left = i+1
            right = n-1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                
                    #skip duplicate values for left and right pointers
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1

                elif total < 0:
                    left += 1
                else:
                    right -= 1
        return res

                                    






        