class Solution:
    def process_string(self, s:str)-> str:
        s = s.lower()
        res = ""
        for i in s:
            if i.isalnum():
                res+=i
        return res

    def isPalindrome(self, s: str) -> bool:
        s = self.process_string(s)
        i = 0
        while i<len(s):
            if s[i]!=s[len(s)-i-1]: return False
            i+=1
        return True