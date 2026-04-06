class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        res = []
        for i, el in enumerate(nums):
            dif = target - el
            if dif in d:
                res += [d[dif], i]
                return res
            else:
                d[el] = i
        return res