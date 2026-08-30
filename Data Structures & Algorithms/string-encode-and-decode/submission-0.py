class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res+=str(len(i))+'#'+i
        return res

    def decode(self, s: str) -> List[str]:
        num = 0
        i = 0
        res = []
        while i<len(s):
            if s[i] != '#':
                num = num*10 + int(s[i])
                i+=1
            else:
                res.append(s[i+1:i+num+1])
                i+=num+1
                num = 0
        return res


                
        
