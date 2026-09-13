class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #so essentially you have to see if the last number is a 9, in that case, you have to see if you have to go toward
        if digits[-1] != 9:
            digits[-1] += 1
            return digits

        else:
            #have to process since ending one is a 9
            cur = len(digits)-1
            keepGoing = True

            while cur > 0:
                #essential go to the left
                digits[cur] = 0
                
                if digits[cur-1] != 9:
                    digits[cur-1] += 1
                    keepGoing = False
                    break

                cur -= 1

            #have to check if leading is 9 and keepGoing
            if digits[0] == 9 and keepGoing:
                digits[0] = 0
                digits.insert(0, 1)
            
            return digits
        