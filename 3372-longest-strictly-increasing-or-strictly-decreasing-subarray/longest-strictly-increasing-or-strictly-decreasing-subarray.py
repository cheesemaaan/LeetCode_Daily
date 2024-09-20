class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc=1
        dec=1
        temp = 1
        for i in range(1,len(nums)):
            if nums[i-1] > nums[i]:
                dec +=1
                temp=max(dec,inc,temp) 
                inc =1
                
            elif nums[i-1] < nums[i]:
                inc +=1
                temp=max(dec,inc,temp)
                dec =1
            else:
                temp=max(dec,inc,temp)
                inc =1
                dec =1  
        
        return temp