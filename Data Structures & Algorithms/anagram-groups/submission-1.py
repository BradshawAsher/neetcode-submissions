from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for char in s:
                count[ord(char) - ord("a")] += 1
            
            #convert list to tuple so it can be hashed as a dict key
            groups[tuple(count)].append(s)

        return list(groups.values())

        