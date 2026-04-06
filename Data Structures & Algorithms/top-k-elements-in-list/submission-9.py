class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        res = []
        for el in nums:
            d[el] = d.get(el, 0) + 1
        vals = sorted(list(d.values()), reverse=True)[:k]
        for k, v in d.items():
            if v in vals:
                res.append(k)
        return res
