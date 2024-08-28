class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        answer = 0
        for i,c in enumerate(zip(startTime,endTime)):
            if startTime[i] <= queryTime and queryTime <= endTime[i]:
                answer +=1
        return answer