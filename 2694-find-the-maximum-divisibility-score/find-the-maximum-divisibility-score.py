class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        d ={}
        for divisor in divisors:
            score = 0
            for num in nums:
                if num%divisor ==0:
                    score +=1
            d[divisor] = score
        # 점수는 내림차순, divisor는 오름차순으로 정렬
        sorted_divisors = sorted(d.items(), key=lambda x: (-x[1], x[0]))
        
        # 첫 번째 항목의 divisor 반환
        return sorted_divisors[0][0]
     
        # score_max = max(d.values())
        # return min(divisor for divisor,score in d.items() if score==score_max)

        
    