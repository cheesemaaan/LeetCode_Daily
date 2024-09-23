class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count_arr =Counter(arr)
        one_value_list =  [x for x in count_arr if count_arr[x] ==1]
        if k <= len(one_value_list):
            answer = one_value_list[k-1]
        else:
            answer = ""
        return answer