# from colelctions import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # using hash map 
        s_map = {}
        for i in s:
            if i not in s_map:
                s_map[i]=1
            else:
                s_map[i]+=1
        if len(t)!=len(s):
            return False
        for i in range(len(t)):
            if t[i] not in s_map:
                return False
            else:
                s_map[t[i]]-=1
            if s_map[t[i]]<0:
                return False
        for s in s_map:
            if s_map[s]!=0:
                return False
        return True
        

        