class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        vowel_list =["a","e","i","o","u"]
        answer  = 0
        for i in range(left,right+1):
            if words[i][0] in vowel_list and words[i][-1] in vowel_list:
                answer +=1
        
        return answer

