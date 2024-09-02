class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        # 첫 번째 좌표의 색을 계산
        color1 = (ord(coordinate1[0])  + int(coordinate1[1])) % 2
        
        # 두 번째 좌표의 색을 계산
        color2 = (ord(coordinate2[0])  + int(coordinate2[1])) % 2
        
        # 두 좌표의 색이 동일한지 확인
        return color1 == color2
