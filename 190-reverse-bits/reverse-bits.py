class Solution:
    def reverseBits(self, n: int) -> int:
        n=f'{n:032b}'
        n=n[::-1]
        n=int(n,2)
        return n
        