class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res+= str(len(i))+i
        return res

    def decode(self, s: str) -> List[str]:
        op = []
        i = 0
        while i<len(s):
            n = int(s[i])
            op.append(s[i+1:i+n+1])
            i += n+1
        
        return op


                
        
