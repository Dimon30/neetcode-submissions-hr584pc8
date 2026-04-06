class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for e in nums:
            d[e] = d.get(e, 0) + 1
        print(d)
        for e in d.values():
            if e > 1:
                return True
        return False