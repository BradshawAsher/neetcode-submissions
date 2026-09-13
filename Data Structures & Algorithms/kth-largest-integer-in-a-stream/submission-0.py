import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        #do we have to sort nums?

        self.min_heap = []

        for num in nums:
            heapq.heappush(self.min_heap, num)

            #keep the heap size at exactly k
            if len(self.min_heap) > k:
                heapq.heappop(self.min_heap)



    def add(self, val: int) -> int:
        #when you add, have to return the kth largest?

        heapq.heappush(self.min_heap, val)

        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        
        return self.min_heap[0]
        
