import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #Sort in-place by distance squared and return the first k elements 
        #if no time/space requirements
        points.sort(key=lambda p: p[0]**2 + p[1]**2)
        return points[:k]

