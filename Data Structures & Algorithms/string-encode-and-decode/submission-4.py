class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs)<1:
            return ""
        res = ""
        for i in strs:
            res+= str(len(i))+"%"+i
        return res

    def decode(self, s: str) -> List[str]:
        if len(s)<=1:
            return [""]

        op = []
        i = 0
        while i<len(s):
            start = i
            end = i
            while s[end]!="%":
                end+=1
            
            n = int(s[start:end])
            
            op.append(s[end+1:end+n+1])
            i = end + n + 1
        
        return op


                
        
