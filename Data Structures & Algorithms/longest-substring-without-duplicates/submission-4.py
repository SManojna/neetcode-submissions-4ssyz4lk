class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0 
        maxLength = 0 
        if len(s)==0 or len(s)==1:
            return len(s)
        while i < len(s):
            substring = set()
            substring.add(s[i])
            j = i+1
            while (j < len(s) and s[j] not in substring):
                substring.add(s[j])
                j+=1
            print(i, j)
            length = j-i
            maxLength = max(maxLength, length)
            print(maxLength)
            i = i+1
        return maxLength
            

        