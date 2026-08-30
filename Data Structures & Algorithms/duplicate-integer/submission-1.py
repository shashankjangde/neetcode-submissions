class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hmap = {i:0 for i in nums}

        for i in nums:
            hmap[i]+=1
            if hmap[i]>1:
                return True
        return False
        