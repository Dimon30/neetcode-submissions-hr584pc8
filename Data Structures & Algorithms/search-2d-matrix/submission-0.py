class Solution:
    def bin_search(self, nums: List[int], target: int) -> bool:
        l = 0
        r = len(nums)-1
        m = l + (r - l) // 2
        while l < r:
            if nums[m] == target:
                return True
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
            m = l + (r - l) // 2
        return nums[m] == target

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if row[0] <= target <= row[-1]:
                print(row)
                return self.bin_search(row, target)
        return False