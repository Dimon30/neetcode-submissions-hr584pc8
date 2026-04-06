class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for el in nums:
            d[el] = d.get(el, 0) + 1
        for _, v in d.items():
            if v > 1: 
                return True
        return False