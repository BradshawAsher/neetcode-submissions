import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #heapq.nlargest(k, nums) returns the k largest element in descending order
        #The last element in that list (index - 1) is the kth largest
        return heapq.nlargest(k, nums)[-1]