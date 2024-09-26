class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        not_dulplicated_nums =[]
        answer=0
        for i in range(len(nums)):
            if i==0:
                not_dulplicated_nums.append(nums[i])
            else:
                if nums[i] !=nums[i-1]:
                    not_dulplicated_nums.append(nums[i])
        
        for i in range(1,len(not_dulplicated_nums)-1):
            if not_dulplicated_nums[i] >not_dulplicated_nums[i-1] and not_dulplicated_nums[i]>not_dulplicated_nums[i+1]:
                answer+=1
            if not_dulplicated_nums[i]<not_dulplicated_nums[i-1] and not_dulplicated_nums[i] <not_dulplicated_nums[i+1]:
                answer+=1    
        return answer