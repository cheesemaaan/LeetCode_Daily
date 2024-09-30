class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        clock =0
        # start가 항상 destination보다 작게 설정
        if start > destination:
            start, destination = destination, start
        
        # 시계 방향 거리
        clock = sum(distance[start:destination])
        
        # 전체 거리에서 시계 방향 거리를 뺀 반시계 방향 거리
        nonclock = sum(distance) - clock
        
        # 더 짧은 거리 반환
        return min(clock, nonclock)
