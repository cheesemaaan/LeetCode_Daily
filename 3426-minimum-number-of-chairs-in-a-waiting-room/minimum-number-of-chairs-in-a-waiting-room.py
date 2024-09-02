class Solution:
    def minimumChairs(self, s: str) -> int:
        answer =[]
        count = 0
        for c in s:
            if c =="E":
                count +=1
                answer.append(count)
            else:
                count -=1
                answer.append(count)
        return max(answer)