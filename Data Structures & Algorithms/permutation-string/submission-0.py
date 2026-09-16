class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #Understand
        #input: s1: smaller str and s2: largest str
        #output: bool (t or f)

        #Time: O(n), where n is the longer of s1 and s2
        #Space: O(1), constant

        #Match - Sliding Window

        #Plan
        #stupid way would to add s1 to a freq map, and when we encounter the first char in s2 that is in s1, then continue to see if everything matches up
        #would have to make a new hash map for each time
        #if we encounter something that is not in it in the middle, then terminate and continue from the right+1

        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False

        s1_counts = [0] * 26
        s2_counts = [0] * 26

        #Initialize frequency for s1 and the first window of s2
        for i in range(n1):
            s1_counts[ord(s1[i]) - ord("a")] += 1
            s2_counts[ord(s2[i]) - ord("a")] += 1
        
        if s1_counts == s2_counts:
            return True

        #slide the window across s2
        for i in range(n1, n2):
            #add new character on the right
            s2_counts[ord(s2[i]) - ord("a")] += 1
            #Remove old character on the left
            s2_counts[ord(s2[i - n1]) - ord("a")] -= 1
        
            #check if counts match
            if s1_counts == s2_counts:
                return True

            
        return False
        


