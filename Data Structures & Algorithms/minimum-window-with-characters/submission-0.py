class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_freqs = {}
        for ch in t:
            t_freqs[ch] = t_freqs.get(ch, 0) + 1
        
        l = 0
        res = "a"*(len(s)+1)
        need = len(t_freqs)
        have = 0
        window_freqs = {}
        for r in range(len(s)):
            window_freqs[s[r]] = window_freqs.get(s[r], 0) + 1
            if s[r] in t_freqs and window_freqs[s[r]] == t_freqs[s[r]]:
               have += 1
            while have==need:
                res = s[l:r+1] if r+1 - l < len(res) else res
                if s[l] in t_freqs and window_freqs[s[l]] == t_freqs[s[l]]:
                    have -= 1 
                window_freqs[s[l]] -= 1
                if window_freqs[s[l]] == 0:
                    del window_freqs[s[l]]
                l += 1
        return res if len(res) <= len(s) else ""