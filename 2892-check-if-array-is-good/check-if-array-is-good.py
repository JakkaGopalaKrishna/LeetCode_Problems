class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()
        m = max(nums)
        if(len(nums)<2):
            return False
        if(nums[-1]==m and nums[-2]==m):
            arr=nums[:len(nums)-2]
            if len(arr)==0:
                return nums[0]==1
            if(len(arr)!=m-1):
                return False
            for i in range(len(arr)):
                if arr[i]!=(i+1):
                    return False
            return True
        else:
            return False