class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        count_max = 0
        for n in nums:
            if n-1 not in set_nums:
                t = n + 1
                count = 1
                while t in set_nums:
                    count += 1
                    t += 1
                if count > count_max:
                    count_max = count
        return count_max