class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        # 한 주기의 길이: 공이 양 끝까지 갔다가 다시 되돌아오는 데 걸리는 시간
        cycle_length = 2 * (n - 1)
        
        # k 초 동안 공이 이동한 위치는 k % cycle_length
        k = k % cycle_length
        
        # 만약 k가 n-1보다 작으면 오른쪽으로 이동 중
        if k <= n - 1:
            return k
        # 그렇지 않으면 다시 왼쪽으로 이동 중이므로
        else:
            return 2 * (n - 1) - k
