import heapq
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [float("inf")] * (n+1)
        dist[k] = 0

        #relax all edges n-1 times
        for _ in range(n-1):
            updated = False

            for u, v, w in times:
                if dist[u] != float("inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    updated = True

            #early exit if distances didn't change
            if not updated:
                break

        #ignore 1-based dummy index 0
        max_dist = max(dist[1:])
        return max_dist if max_dist != float("inf") else -1

