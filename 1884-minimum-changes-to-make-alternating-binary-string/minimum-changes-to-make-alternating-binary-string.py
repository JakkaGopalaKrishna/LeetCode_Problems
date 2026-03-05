class Solution:
    def minOperations(self, s: str) -> int:
        check = 0
        num1 = 0
        num2 = 0
        for num in s:
            n = int(num)
            num1+=n^check
            if check:
                check = 0
            else:
                check = 1
            num2+=n^check
        return num1 if num1<num2 else num2