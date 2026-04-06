class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for n in nums:
            d[n] = d.get(n, 0) + 1
        t = [[] for i in range(len(nums)+1)]
        for key, value in d.items():
            t[value].append(key)

        res = []
        for i in range(len(t)-1, 0, -1):
            for n in t[i]:
                res.append(n)
                if len(res) == k:
                    return res