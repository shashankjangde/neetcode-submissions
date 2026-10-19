class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs)<1:
            return ""
        res = ""
        for i in strs:
            res+= str(len(i))+i
        return res

    def decode(self, s: str) -> List[str]:
        if len(s)<=1:
            return [""]

        op = []
        i = 0
        while i<len(s):
            start = i
            end = i
            while s[end+1] in "0123456789":
                end+=1
            
            n = int(s[start:end+1])
            
            op.append(s[i+1:i+n+1])
            i += n+1
        
        return op


                
        
