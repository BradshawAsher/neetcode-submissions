class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        #freq buckets: index 0 to len(nums)
        buckets = [[] for _ in range(len(nums)+1)]

        #1. Count frequencies
        for n in nums:
            count[n] = count.get(n, 0) + 1

        #2. Place numbers into buckets matching their frequencies
        for n, c in count.items():
            buckets[c].append(n)

        #traverse buckets from highest frequency to lowest
        res = []
        for i in range(len(buckets)-1, 0, -1):
            for n in buckets[i]:
                res.append(n)
                if len(res) == k:
                    return res
