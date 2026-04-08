import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub(r'[^\w\n]','',s)
        l = len(s)
        mid = l//2
        return s[:mid] == s[l-mid:][::-1]

        