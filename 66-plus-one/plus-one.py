class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits=''.join(str(n) for n in digits)
        digits=int(digits)
        digits+=1
        return [int(n) for n in str(digits)]
