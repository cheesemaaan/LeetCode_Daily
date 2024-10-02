class Solution:
    def search(self, nums: List[int], target: int) -> int:
        indices = [i for i, num in enumerate(nums) if num == target]
        answer = indices[0] if indices else -1
        print(answer)
        return answer