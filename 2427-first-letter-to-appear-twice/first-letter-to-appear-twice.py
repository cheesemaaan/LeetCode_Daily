class Solution:
    def repeatedCharacter(self, s: str) -> str:
        count_dict = {}
        for c in s:
            if c not in count_dict:
                count_dict[c]=[1]
            else:
                return c
        
        

