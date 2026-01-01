class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num_string=''.join(str(n) for n in digits)
        num=int(num_string)
        num+=1
        return [int(n) for n in str(num)]
