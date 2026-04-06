class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            word = "".join(sorted(s))
            d[word] = d.get(word, []) + [s]
        return [val for val in d.values()]