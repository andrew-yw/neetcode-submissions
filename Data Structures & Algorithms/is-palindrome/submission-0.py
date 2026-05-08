class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char for char in s if char.isalnum())
        for i in range(len(s)//2):
            reverse = -i-1
            if s[i].lower() != s[reverse].lower():
                return False
        return True
            