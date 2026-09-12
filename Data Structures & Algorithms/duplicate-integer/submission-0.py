from collections import * 
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #we can use a set 


        values = set()

        for num in nums:
            if num not in values:
                values.add(num)
            else:
                return True
        
        return False
