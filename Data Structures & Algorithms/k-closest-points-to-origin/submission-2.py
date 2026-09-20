import random
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def dist(p: List[int]) -> int:
            return p[0] * p[0] + p[1] * p[1]

        def partition(left: int, right: int, pivot_idx: int) -> int:
            pivot_dist = dist(points[pivot_idx])

            #1. Move pivot out of the way to the end
            points[pivot_idx], points[right] = points[right], points[pivot_idx]

            #2. Shift all elements smaller than the pivot to the left
            store_idx = left

            for i in range(left, right):
                if dist(points[i]) <= pivot_dist:
                    points[store_idx], points[i] = points[i], points[store_idx]
                    store_idx += 1

            #3. Place pivot into its final resting position
            points[store_idx], points[right] = points[right], points[store_idx]
            return store_idx

        left, right = 0, len(points) - 1
        target = k-1 #0-indexed target position

        while left <= right:
            #pick a random pivot to avoid O(N^2) worst-case on sorted data
            pivot_idx = random.randint(left, right)
            pivot_idx = partition(left, right, pivot_idx)

            if pivot_idx == target:
                break

            elif pivot_idx < target:
                left = pivot_idx + 1 #target is in the right partition

            else:
                right = pivot_idx - 1 #target is in the left position

        return points[:k]

