import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = nums

        #Turn the entire list into a min-heap in O(n) time
        heapq.heapify(self.min_heap)

        #pop down until only the k largest elements remain
        while len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        
        if len(self.min_heap) < self.k:
            heapq.heappush(self.min_heap, val)
        elif val > self.min_heap[0]:
            #only push if val is larger than the current kth largest
            heapq.heappushpop(self.min_heap, val)
        
        return self.min_heap[0]
        
