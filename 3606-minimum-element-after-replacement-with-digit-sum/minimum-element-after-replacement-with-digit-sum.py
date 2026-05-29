class Solution:
    def minElement(self, nums: List[int]) -> int:
        re=1000
        for i in nums:
            su=sum([int(n) for n in str(i)])
            if(re>su):
                re=su
        return re