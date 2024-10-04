class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j] == target:
        #             return [i,j]

        d= defaultdict(list)
        for i, num in enumerate(nums):
            d[num].append(i)

        test = 0
        for i,num in enumerate(nums):
            test = target - num
            if test in d :
                if i!=d[test][0]:
                    return [i,d[test][0]]
            else:
                continue       