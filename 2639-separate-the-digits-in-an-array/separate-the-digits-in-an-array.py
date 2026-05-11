class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        s=''
        for i in nums:
            s+=str(i)
        return [int(i) for i in s]