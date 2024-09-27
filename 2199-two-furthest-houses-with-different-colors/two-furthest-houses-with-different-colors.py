class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        max_distance = 0
        n =len(colors)
        for i in range(n):
            print(i,"check")
            for j in range(i+1,n):
                if colors[i] != colors[j] and abs(i-j) > max_distance:
                    max_distance = max(max_distance,abs(i-j))
                    print(max_distance)
        
        return max_distance

