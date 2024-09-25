class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        answer=[]
        for i in range(1,len(height)):
            if height[i] != 0 and height[i-1]>threshold:
                answer.append(i)
        
        return answer