class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        count = 0
        idx = None
        for i, n in enumerate(nums):
            if n == 0:
                count += 1
                if count >= 2:
                    return [0] * len(nums)
                idx = i
                continue
            product *= n
        if count == 1:
            res = [0] * len(nums)
            res[idx] = product
            return res
        res = []
        for n in nums:
            res.append(product // n)
        return res