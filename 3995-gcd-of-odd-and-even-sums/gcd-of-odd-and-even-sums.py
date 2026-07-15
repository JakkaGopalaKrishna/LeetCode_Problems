class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        return gcd(o:=sum(v%2*v for v in range(1,2*n,2)),sum(range(2*n))-o)