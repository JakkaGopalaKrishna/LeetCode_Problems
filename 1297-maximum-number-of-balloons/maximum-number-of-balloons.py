class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        a = text.count('a')
        b = text.count('b')
        n = text.count('n')
        l = text.count('l')//2
        o = text.count('o')//2
        return min(a,b,n,l,o)