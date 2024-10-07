class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        d ={}
        for divisor in divisors:
            score = 0
            for num in nums:
                if num%divisor ==0:
                    score +=1
            d[divisor] = score
        print(d)
        
        answer = inf
        if d.values():
            score_max = max(d.values())
        else:
            return 0
        for num,cnt in d.items():
            if cnt == score_max:
                answer = min(answer,num)

        return answer


        
    