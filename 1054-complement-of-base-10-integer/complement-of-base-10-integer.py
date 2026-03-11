class Solution:
    def bitwiseComplement(self, n: int) -> int:
        val= bin(n)[2:].replace('1','2')
        val = val.replace('0','1')
        val = val.replace('2','0')
        return int(val,2)