class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        count = 0
        idx = None
        res = []

        for i, el in enumerate(nums):
            if el == 0:
                count += 1
                if count == 2:
                    return [0]*len(nums)
                idx = i
                continue
            prod *= el

        if count == 1:
            res = [0]*len(nums)
            res[idx] = prod
            return res

        for el in nums:
            res.append(prod//el)
        
        return res