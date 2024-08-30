class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        sorted_nums = sorted(nums)
        answer = 0
        for num in sorted_nums:
            if num <k:
                answer +=1
                
            else:
                break
        return answer