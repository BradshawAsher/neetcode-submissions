import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        #Min-heap stores (frequency, num) of size k
        return heapq.nlargest(k, count.keys(), key=count.get)