class Solution:
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = self.getNext(n)

        #fast pointer moves two steps, slow moves one step
        while fast != 1 and slow != fast:
            slow = self.getNext(slow)
            fast = self.getNext(self.getNext(fast))

        #if the fast reached 1, it's a happy number; if slow == fast != 1, there's a cycle
        return fast == 1


    def getNext(self, n: int) -> int:
        #take the %10, then // 10
        total_sum = 0

        while n > 0:
            cur = n % 10
            total_sum += cur ** 2
            n = n // 10
        
        return total_sum
        