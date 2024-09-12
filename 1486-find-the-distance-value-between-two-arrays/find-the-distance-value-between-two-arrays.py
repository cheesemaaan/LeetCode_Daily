class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        count = 0
        answer = 0
        for a1 in arr1:
            for a2 in arr2:
                if abs(a1-a2) > d:
                    count+=1
                    continue
                else:
                    break
            if count == len(arr2):
                answer+=1
            count = 0
        return answer