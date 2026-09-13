class Solution:
    def countBits(self, n: int) -> List[int]:
    

        output = [0] * (n+1)


        #i guess work your way up
        for i in range(n+1):
            count = 0
            copy = i
            while copy:
                copy = copy & (copy-1) #or i &= i-1
                count += 1
            output[i] = count
        
        return output

