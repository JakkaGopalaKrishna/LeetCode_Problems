class Solution:
    def numberOfSpecialChars(self, w: str) -> int:
        return sum(0 <= w.rfind(l) < w.find(u) for l,u in zip(ascii_lowercase, ascii_uppercase))