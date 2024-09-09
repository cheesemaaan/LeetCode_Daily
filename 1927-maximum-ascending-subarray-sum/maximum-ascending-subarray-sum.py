class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        prev = 0
        cur_sum = 0
        answer = 0
        for num in nums:
            if num> prev:
                cur_sum += num
                answer = max(cur_sum,answer)

            else:
                cur_sum = num
            
            prev = num
        
        return answer
                

            