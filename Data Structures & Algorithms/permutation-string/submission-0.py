class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d = {}
        for ch in s1:
            d[ch] = d.get(ch, 0) + 1

        l = 0
        k = len(s1)
        window_freqs = {}

        for r in range(len(s2)):
            window_freqs[s2[r]] = window_freqs.get(s2[r], 0) + 1

            if r - l + 1 > k:
                window_freqs[s2[l]] -= 1
                if window_freqs[s2[l]] == 0:
                    del window_freqs[s2[l]]
                l += 1

            if r - l + 1 == k and window_freqs == d:
                return True

        return False