class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        count = 0
        
        for num in nums:
            # num - k나 num + k가 이미 존재하는 경우 쌍을 형성할 수 있음
            count += freq[num - k]
            count += freq[num + k]
            
            # 현재 숫자의 빈도를 증가
            freq[num] += 1
        
        return count