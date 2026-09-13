class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #so essentially you have to see if the last number is a 9, in that case, you have to see if you have to go toward
        for i in range(len(digits)-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            
            #else
            digits[i] = 0

        
        #if all digits were 9, prepend 1
        return [1] + digits
        