class Solution:
    def isHappy(self, n: int) -> bool:
        #use visited set
        #if number is in visited, then return false
        #if it stops at 1, then return true
        visited = set()

        while n not in visited and n != 1:
            visited.add(n)
            n = self.process(n)
        
        if n == 1:
            return True
        return False


    def process(self, n: int) -> int:
        #take the %10, then // 10
        sum = 0

        while n > 0:
            cur = n % 10
            sum += cur ** 2
            n = n // 10
        
        return sum
        