class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {i: {j: 0 for j in i} for i in strs}

        for i in strs:
            for j in i:
                hmap[i][j] += 1

        res = []

        for i in range(len(strs)):
            if hmap[strs[i]] == dict():
                continue

            x = [strs[i]]

            for j in range(i + 1, len(strs)):
                if hmap[strs[i]] == hmap[strs[j]]:
                    x.append(strs[j])
                    hmap[strs[j]] = dict()

            res.append(x)
            hmap[strs[i]] = dict()

        return res