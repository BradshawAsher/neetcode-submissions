class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #non decreasing
        #Understand
        #input = list non-decreaisng ascending(order)
        #output = list of length 2 of the 1-indexed pos of the 2 numbers who add up to the target

        #m - match = two pointers
        #Plan 
        #cannot use same element twice


        #[1, 3, 5, 7, 9] target = 12

        #start 2 pointers, one at the beginning and one at the end and shift depending on bigger or smaller 
        #if the sum < target, move the left += 1. otherwise, move the right -= 1

        left = 0
        right = len(numbers) - 1

        while left < right:
            total = numbers[left] + numbers[right]
            if total == target:
                return [left+1, right+1]

            elif total < target:
                left += 1
            
            else:
                right -= 1
            

        return [left+1, right+1]












        