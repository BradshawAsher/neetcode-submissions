from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #we can use a frequency map and then subtract from each
        #first count s into a freq map
        #then count items of t and remove values from freqmap if found, if negative values, return false
        #only return True if freq map is empty at the end
        return Counter(s) == Counter(t)



