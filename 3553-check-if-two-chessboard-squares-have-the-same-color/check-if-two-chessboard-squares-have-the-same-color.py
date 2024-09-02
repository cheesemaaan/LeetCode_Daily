class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
       x_1,y_1 = coordinate1
       x_2,y_2 = coordinate2
       color1 = (ord(x_1)+int(y_1))%2
       color2 = (ord(x_2)+int(y_2))%2
       return color1 == color2
