class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d_s = {}
        d_t = {}
        for el in s.strip():
            d_s[el] = d_s.get(el, 0) + 1
        for el in t.strip():
            d_t[el] = d_t.get(el, 0) + 1
        return d_s == d_t