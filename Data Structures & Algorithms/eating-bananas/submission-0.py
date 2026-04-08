class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 0
        r = max(piles)

        while r - l > 1:
            k = l + (r-l) // 2
            t = sum([p//k + (1 if p%k != 0 else 0) for p in piles])
            if t > h:
                l = k
            else:
                r = k
        return r