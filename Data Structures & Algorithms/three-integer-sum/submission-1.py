class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)
        for i in range(n):
            target = -nums[i]
            l = i+1
            r = n-1
            while l < r:
                if nums[l] + nums[r] == target and [nums[i], nums[l], nums[r]] not in res:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1

                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    l += 1
        return res