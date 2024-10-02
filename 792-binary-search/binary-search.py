class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r= len(nums) -1
        answer = 0
        while l<=r: 
            mid =(l+r)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid-1 #무한루프 방지를 위해 
            elif nums[mid] < target:
                l = mid+1
        return -1