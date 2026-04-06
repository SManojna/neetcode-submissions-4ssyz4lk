class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_dict = {}
        l1, l2 = len(s), len(t)
        if l1!=l2:
            return False
        for i in range(0,l1):
            if s[i] not in char_dict:
                char_dict[s[i]]=1
            else:
                char_dict[s[i]]+=1
        # print(char_dict)
        for i in range(0,l2):
            # print(t[i])
            if t[i] not in char_dict:
                return False
            else:
                char_dict[t[i]]-=1
            if char_dict[t[i]]<0:
                return False
        return True



        