class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        answer =[]
        nums_dict=Counter(nums)
        for num,cnt in nums_dict.items():
            if cnt >= 2:
                answer.append(num)

        return answer