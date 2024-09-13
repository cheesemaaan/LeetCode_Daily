class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # answer = 0
        # if 0 in nums:
        #     answer = len(set(nums))-1
        # else:
        #     answer =len(set(nums))
        return len(set(nums)) -(1 if 0 in nums else 0)