class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        even_nums = [x for x in nums if x%2 ==0]
        cnt = Counter(even_nums)
        if  not even_nums:
            return -1
        max_value = max(cnt.values())
        answer =[cnt for cnt,value in cnt.items() if value==max_value]
        return min(answer)


    