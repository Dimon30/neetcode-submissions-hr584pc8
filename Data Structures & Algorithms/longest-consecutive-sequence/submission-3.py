class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        m = min(nums)
        M = max(nums)
        ar = [0]*(M - m + 1)
        for el in nums:
            ar[el - m] += 1
        print(ar)
        count = 0
        res = -1
        for el in ar:
            if el > 0:
                count += 1
            else:
                if res >= count:
                    count = 0
                else:
                    res = count
                    count = 0
        return max(res, count)