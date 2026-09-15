import heapq
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #1. Build adjacency list: u -> list of (weight, v)
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((w, v))

        #2. Min-heap stores: (current_travel_time, node)
        min_heap = [(0, k)]
        visited = set()
        max_time = 0

        while min_heap:
            time, node = heapq.heappop(min_heap)

            if node in visited:
                continue
            
            visited.add(node)
            max_time = time

            #If all n nodes are visited, we can stop early
            if len(visited) == n:
                return max_time

            for weight, neighbor in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (time + weight, neighbor))

        #if not all n nodes could be reached
        return max_time if len(visited) == n else -1

