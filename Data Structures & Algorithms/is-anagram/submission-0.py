class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #we can use a frequency map and then subtract from each
        #first count s into a freq map
        #then count items of t and remove values from freqmap if found, if negative values, return false
        #only return True if freq map is empty at the end
        if len(s) != len(t):
            return False

        freq_map = {}

        for char in s:
            freq_map[char] = freq_map.get(char, 0) + 1
        
        for char in t:
            if char not in freq_map or freq_map[char] == 0:
                return False
            
            freq_map[char] = freq_map[char]-1
        
        return True



