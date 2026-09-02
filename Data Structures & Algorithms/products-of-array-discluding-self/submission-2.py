class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]*len(nums)
        right = [1]*len(nums)
        for i in range(1,len(nums)):
            left[i] = left[i-1]*nums[i-1]
            right[len(right)-1-i] = right[len(right)-i]*nums[len(right)-i]
        
        res = []
        for i in range(len(nums)):
            res.append(left[i]*right[i])
        return res