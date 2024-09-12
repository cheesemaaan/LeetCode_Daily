class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        arr_dict = {}
        up = 0
        for  c in sorted(set(arr)):
            up+=1
            arr_dict[c] = up
        
        return [arr_dict[num] for num in arr]