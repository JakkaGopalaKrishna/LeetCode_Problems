
class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        digits.sort()
        even_digits = [d for d in set(digits) if d % 2 == 0]
        result = set()
    
        for last_digit in even_digits:
            temp_digits = digits.copy()
            temp_digits.remove(last_digit)
    
            for first, second in itertools.permutations(temp_digits, 2):
                if first != 0:
                    num = first * 100 + second * 10 + last_digit
                    result.add(num)
    
        return len(result)