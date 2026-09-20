import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #kth largest element in array
        #O(nlogk) time and O(k) space at least, n = arr size and k = rank of largest number (k)

        #so we probably need a similar method of max heap and then heappushpop when we find an element that is greater than it

        #like since our heap will be of size k and the root will be the element to be returned
        #we will add to heap if the heap is not yet at size k, and otherwise, we compare the newest value with the heap root. If the value > root, then we can heappushpop
        min_heap = nums[:k]
        heapq.heapify(min_heap)

        for num in nums[k:]:
            if num > min_heap[0]:
                heapq.heappushpop(min_heap, num)

        return min_heap[0]