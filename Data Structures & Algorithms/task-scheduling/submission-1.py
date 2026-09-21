import heapq
from collections import Counter, deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)

        #Max-heap storing negative counts
        max_heap = [-cnt for cnt in counts.values()]
        heapq.heapify(max_heap)

        #queue stores: (remaining_count, available_at_time)
        q = deque()
        time = 0

        while max_heap or q:
            time += 1

            #1. If we can run a task from the heap, pick the most frequent
            if max_heap:
                cnt = 1 + heapq.heappop(max_heap) #Decrement frqeuency (toward 0)
                if cnt < 0:
                    q.append((cnt, time + n))
            
            #2. Check if any cooled-down task is ready to re-enter the heap
            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])

        return time