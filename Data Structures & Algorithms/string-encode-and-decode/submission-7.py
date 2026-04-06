class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "nan"
        return ";".join(strs)
    def decode(self, s: str) -> List[str]:
        if s == "nan":
            return []
        return s.split(";")