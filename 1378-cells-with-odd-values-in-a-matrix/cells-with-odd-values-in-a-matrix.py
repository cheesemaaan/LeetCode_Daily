class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        mat = [[0 for i in range(n)] for j in range(m)]
        for row,col in indices:
            for i in range(n):
                mat[row][i] +=1
            for j in range(m):
                mat[j][col] +=1
        answer =0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] % 2 ==1:
                    answer+=1
        return answer