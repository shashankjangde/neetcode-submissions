class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = dict()

        for i in nums:
            if i not in hmap:
                hmap[i] = 0

            hmap[i]+=1
        
        hmap = {k:v for k,v in sorted(hmap.items(),key = lambda item: item[1], reverse = True)}
        output = list(hmap.items())[:k]

        res = [i for i,_ in output]
        return res

        
