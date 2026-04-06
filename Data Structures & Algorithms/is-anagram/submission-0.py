class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1, d2 = {}, {}
        for e in s:
            d1[e] = d1.get(e, 0) + 1
        for e in t:
            d2[e] = d2.get(e, 0) + 1
        return d1 == d2