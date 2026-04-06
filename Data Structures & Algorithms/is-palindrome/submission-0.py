class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        s = re.sub("[^a-zA-Z0-9]", "", s).lower()
        for i in range(len(s)//2):
            if s[i] != s[len(s)-i-1]:
                return False
        return True