class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        st = list(set(nums))
        cur = 0
        mxsq = 0
        cur_len = 0
        while cur<len(st)-1:
            if st[cur]+1 == st[cur+1]:
                cur_len+=1
                cur += 1
            else:
                mxsq = max(mxsq, cur_len+1)
                cur_len=0
                cur += 1
            
        return max(mxsq, cur_len+1)



            
        