
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1

        #Sort items by frequencies (x[1]) in descending order

        sorted_items = sorted(freq_map.items(), key=lambda x: x[1], reverse=True)

        res = []
        for i in range(k):
            #sorted_items[i] is a tuple (num, count)
            res.append(sorted_items[i][0])

        return res