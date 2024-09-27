class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        answer =-1
        for i,num in enumerate(nums):
            if i%10 == num:
                answer = i
                break
        return answer