class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        num_set = set(nums)
        best = 0
        for el in num_set:
            if el-1 not in num_set:
                cur = el
                while cur in num_set:
                    cur += 1
                best = max(best, cur - el)
        return best