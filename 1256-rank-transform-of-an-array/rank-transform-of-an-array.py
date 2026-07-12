class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_arr = sorted(set(arr))
    
    # Create a dictionary that maps each element to its rank
        rank_dict = {num: rank + 1 for rank, num in enumerate(sorted_arr)}
    
    # Replace each element in the original array with its rank
        return [rank_dict[num] for num in arr]