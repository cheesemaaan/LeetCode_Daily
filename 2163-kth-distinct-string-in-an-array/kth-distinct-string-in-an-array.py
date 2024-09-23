class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count_arr =Counter(arr)
        print(count_arr)
        one_value_list =  [a for a,cnt in count_arr.items() if cnt ==1]
        if k <= len(one_value_list):
            answer = one_value_list[k-1]
        else:
            answer = ""
        return answer