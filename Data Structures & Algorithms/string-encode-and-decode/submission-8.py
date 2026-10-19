class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs)<1:
            return ""
        delim = "|"
        res = ""
        for i in strs:
            for j in i:
                if j == delim or j == "\\":
                    res+="\\"
                res+=j
            res+=delim
        return res

    def decode(self, s: str) -> List[str]:
        if len(s)==0:
            return []
        if len(s)==1:
            return [""]

        op = []
        word = ""
        i = 0
        while i<len(s):
            if s[i] == "|":
                op.append(word)
                word = ""
                i+=1
                continue
            elif s[i] == "\\":
                i+=1
            word+=s[i]
            i+=1
        return op



                
        
