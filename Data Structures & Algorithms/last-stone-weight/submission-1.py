import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #1. Invert signs to simulate a max-heap using Python's min-heap
        max_heap = [-s for s in stones]
        heapq.heapify(max_heap)

        #2. smash stones while at least two stones remain
        while len(max_heap) > 1:
            first = -heapq.heappop(max_heap) #heaviest stone
            second = -heapq.heappop(max_heap) #second heaviest stone

            if first > second:
                #push the remaining weight back into the heap (inverted)
                heapq.heappush(max_heap, -(first-second))

        #3. return the last remaining stone, or 0 if no stones left
        return -max_heap[0] if max_heap else 0
        