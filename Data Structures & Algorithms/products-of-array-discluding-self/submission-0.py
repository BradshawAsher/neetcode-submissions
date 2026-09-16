class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #stupid way first
        #loop through and find the product of all, then loop again and divdie by ecah number to replace
        prod = 1

        #if there are more than 2 zeros, then everythinig is a zero
        num_zeros = 0

        for num in nums:
            #prod *= num if num is not 0. If num is 0, then add to num_zeros but don't change prod
            if num != 0:
                prod *= num
            else:
                num_zeros += 1

        #now in-place replacing
        for i in range(len(nums)):
            #if we have 2 or more zeros, everything is 0
            if num_zeros >= 2:
                nums[i] = 0
            
            elif num_zeros == 1:
                if nums[i] == 0:
                    nums[i] = prod
                else:
                    nums[i] = 0
            else:
                nums[i] = int(prod / nums[i])
        
        return nums