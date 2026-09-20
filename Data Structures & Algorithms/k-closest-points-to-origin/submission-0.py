import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #closest to origin (0, 0)
        #solution as good or better than O(nlogk) time and O(k) space, where n is the size of the input arr and k is the # of points to be returned

        #so can't we just have a min heap of tuples (dist, point) of max size k and then like heappop or heappush and stuff like that
        #no idea how to do it though
        #use max heap

        #Max-heap storing tuples: (-distance_squared, [x, y])
        max_heap = []

        for x, y in points:
            dist_sq = x*x + y*y

            #If we haven't reached k points yet, simply push
            if len(max_heap) < k:
                heapq.heappush(max_heap, (-dist_sq, [x, y]))
            else:
                #If the current point is closer than the farthest point in our heap
                #(Note: max_heap[0][0] is negative, so -max_heap[0][0] is the positive farthest distance)
                if dist_sq < -max_heap[0][0]:
                    heapq.heappushpop(max_heap, (-dist_sq, [x, y]))

        #Extract the k points from the heap
        return [point for _, point in max_heap]

