from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #O(m) time and O(1) space, where m is the size of the tasks arr
        freqs = Counter(tasks)
        max_freq = max(freqs.values())

        #How many distinct tasks share this max frequency?
        max_count = sum(1 for count in freqs.values() if count == max_freq)

        #The answer is bounded below by the structured slots or total tasks
        return max(len(tasks), (max_freq-1) * (n+1) + max_count)