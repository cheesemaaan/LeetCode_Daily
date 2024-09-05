class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        mat = [[0 for _ in range(n)] for _ in range(m)] 
        for row,col in indices:
            for j in range(n):
                mat[row][j] +=1
            for i in range(m):
                mat[i][col]+=1
        answer = 0
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] % 2 == 1:
                    answer +=1    
        
        return answer