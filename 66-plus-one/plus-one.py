class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num_string=''.join(str(n) for n in digits)
        num_string=int(num_string)
        num_string+=1
        return [int(n) for n in str(num_string)]
