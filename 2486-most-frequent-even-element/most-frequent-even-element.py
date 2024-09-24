class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        answer =[]
        even_nums = [x for x in nums if x%2 ==0]
        cnt = Counter(even_nums)
        print(cnt)
        if  not even_nums:
            return -1
        max_value = max(cnt.values())
        for cnt,value in cnt.items():
            if value==max_value:
                answer.append(cnt)
        
        
        return min(answer)


    