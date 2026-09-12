class Solution:
    def isPalindrome(self, s: str) -> bool:
        #two pointer, one on the left and one on the right

        new_s = "".join(ch.lower() for ch in s if ch.isalnum())

        left = 0
        right = len(new_s)-1

        #case insensitive
        while left < right:
            left_val = new_s[left]
            right_val = new_s[right]

            if left_val != right_val:
                return False
            
            left += 1
            right -= 1
        
        return True
