class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #sliding window
        #Understand
        #input: s -> str, uuppercase english chars
        #input: k = k replacements
        #ouput: int for longest len of substring w/ 1 char

        #match - sliding window

        #plan - O(n) time and O(m) space -> n = length, m = # of unique chars in the string
        count = {}
        max_len = 0
        max_freq = 0
        left = 0

        for right in range(len(s)):
            #1. Expand window and update frequency
            count[s[right]] = count.get(s[right], 0) + 1
            max_freq = max(max_freq, count[s[right]])

            #2. If invalid, shrink the window from the left
            #Window length is (right - left + 1)
            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1

            #3. Update the max valid window seen so far
            max_len = max(max_len, right - left + 1)

        return max_len
        