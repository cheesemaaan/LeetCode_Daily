class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        cur_loc = 1
        cnt = 0
        visited = set([cur_loc])
        
        while True:
            cnt += 1
            cur_loc = (cur_loc + cnt * k - 1) % n + 1  # 1-based 인덱싱 유지
            
            if cur_loc in visited:
                break
            visited.add(cur_loc)
        
        # 공을 받지 못한 친구들 찾기
        return sorted([i for i in range(1, n + 1) if i not in visited])
