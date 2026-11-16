class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_len = 0
        seen = set()
        left, rght = 0,0

        #rght is our exploratory pointer

        while rght < len(s):
            if s[rght] in seen:
                while s[rght] in seen:
                    seen.remove(s[left])
                    left += 1
            
            seen.add(s[rght])
            longest_len = max(longest_len, rght+1-left)
            rght += 1
        
        return longest_len
        
                