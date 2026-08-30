class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hmap = {i:0 for i in s}
        for i in s:
            hmap[i]+=1
        
        for i in t:
            if  (i not in hmap) or (hmap[i]==0):
                return False
            hmap[i]-=1
        
        if sum(hmap.values()) == 0:
            return True
        return False
        