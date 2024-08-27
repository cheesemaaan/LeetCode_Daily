class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        while k!= 0:
            min_value = min(nums)
            for i,num in enumerate(nums):
                if num == min_value:
                    nums[i] = min_value*multiplier
                    break
            k -=1
        

        return nums
