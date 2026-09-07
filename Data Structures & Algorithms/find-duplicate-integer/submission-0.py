class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ht = dict()
        for i in nums:
            if i not in ht:
                ht[i]=1
            else:
                ht[i]+=1 
        
        for i,j in ht.items():
            if j>1:
                return i
        