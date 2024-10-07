class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        d ={}
        for divisor in divisors:
            score = 0
            for num in nums:
                if num%divisor ==0:
                    score +=1
            d[divisor] = score
        
        answer = inf
        score_max = max(d.values())
        for num,cnt in d.items():
            if cnt == score_max:
                answer = min(answer,num)

        return answer


        
    