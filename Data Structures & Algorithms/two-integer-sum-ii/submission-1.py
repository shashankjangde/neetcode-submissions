class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        prx = [0]*len(numbers)
        hs = dict()
        prev = 0
        for i in range(len(numbers)):
            hs[numbers[i]] = i
            prx[i] = numbers[i] + prev
            prev = numbers[i]
        
        for i in range(len(numbers)):
            check = target - numbers[i]
            if check in hs:
                return [i+1, hs[check]+1]
        