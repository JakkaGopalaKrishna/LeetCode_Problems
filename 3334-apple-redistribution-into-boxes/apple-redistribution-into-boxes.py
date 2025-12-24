class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        re=0
        s=sum(apple)
        capacity.sort()
        for i in range(len(capacity)-1,-1,-1):
            re+=1
            s-=capacity[i]
            if s<=0:
                return re
